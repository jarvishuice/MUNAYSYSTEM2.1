import threading
from core.Entities.reports.coffeshop.cofeshopReportEntity import ReporteCoffeshopEntity
import datetime
from config.Logs.LogsActivity import Logs

class PlantillaHTMLPreCierreJornada():
    def __init__(self):
        pass
    def procesarVentasPorCliente(self,datos:ReporteCoffeshopEntity):
     self.totalGlobal =0
     self.ordenesClose=''
     if datos.ventasPorCliente is not None:
      for i in datos.ventasPorCliente:
            self.ordenesClose+=f"""<tr><td colspan="4" >{i.cliente}</td><td colspan="4" >{i.total}</td></tr>"""
            self.totalGlobal+=i.total
    def procesar_ordenes_abiertas(self, datos:ReporteCoffeshopEntity):
        self.OrdenesAbiertas = ''
        self.totalOrdenesAbiertas = 0
        
        for ii in datos.ordenesAbiertas:
            self.OrdenesAbiertas += f"""<tr> <td>{ii.idOrden}</td>
            
            <td>{ii.cliente}</td>
            <td>{ii.total}</td>
            <td>{ii.fecha}</td>
            <td>{ii.hora}</td>
            </tr>"""
            # sumatoria de las ordenes Abiertas
            self.totalOrdenesAbiertas += ii.total
   
           
    def procesarDetallesPagos(self,datos:ReporteCoffeshopEntity):
      #self.Pagos=[]
      self.totalPAYPAL=0
      self.PAGOSGLOBAL=0
      self.pagos=''
      self.totalZELLE=0
      self.TRANSFERENCIAPANAMA=0
      self.TRANSFERENCIANACIONAL=0
      self.TRANSFERENCIABOFA=0
      self.EFECTIVODIVISA=0
      self.EFECTIVOBS =0
      self.punto=0
      self.PAGOMOVIL=0
      self.totalWALLET=0
      
      for i in datos.detallePagos:  
            Logs.WirterTask(str(i.metodo)+'esete')
            self.PAGOSGLOBAL+=i.monto
            #self.pagos+=f"""<tr><td>{i.cliente}</td><td>{i.monto} $</td><td>{round((i.monto) * (i.cotizacion),2)} bs</td><td>{i.cotizacion}</td><td>{i.motivo}</td><td>{i.metodo}</td> <td>{i.banco}</td><td>{i.referencia}</td></tr>"""
            
            match i.metodo:
             case 'PAY-PAL':
                self.totalPAYPAL+=i.monto
             case 'ZELLE':
                   self.totalZELLE+=i.monto
          
             case 'TRANSFERENCIA PANAMA':
              
                   self.TRANSFERENCIAPANAMA+=i.monto
             case 'TRANSFERENCIA NACIONAL':
                   self.TRANSFERENCIANACIONAL+=i.monto
             case 'TRANSFERENCIA BOFA':
                   self.TRANSFERENCIABOFA +=i.monto
             case'EFECTIVO $':
                   self.EFECTIVODIVISA +=i.monto
             case 'EFECTIVO BS':
                   self.EFECTIVOBS +=i.monto
             case 'PUNTO DE VENTA':
                   Logs.WirterTask(f"este es {i.monto}")
                   self.punto +=i.monto
             case 'PAGO MOVIL':
                   self.PAGOMOVIL +=i.monto
             case 'wallet'  :
               if i.monto  >= 0 :
                 self.totalWALLET += i.monto
               else:
                 pass
      
      
    @classmethod
    def procesar_punto_count(self, datos:ReporteCoffeshopEntity):
        self.puntoCount = ''
        
        for i in datos.puntoCount:
            self.puntoCount += f"""<tr><td class='total'>{i.cantidad}</td><td class ='total'>{round(i.monto,2)}.Bs</td></tr>"""
    
    def getHTML(self, datos: ReporteCoffeshopEntity,sede:str):
        self.style = """<style>
        body {
          font-family: Arial, sans-serif;
        }
        
        table {
          border-collapse: collapse;
          width: 90%;
          margin-left:5%;
        }
        
        th, td {
          border: 1px solid black;
          padding: 1px 1px 1px;
          text-align: center;
        }
        
        th {
          background-color: #4682b4;
        }
        
        .total {
          font-weight: bold;
        }
        
        </style>"""
        
        # Crear hilos para procesar las órdenes abiertas y el punto count
        hilo_ordenes_abiertas = threading.Thread(target=self.procesar_ordenes_abiertas, args=(datos,))
        hilo_punto_count = threading.Thread(target=self.procesar_punto_count, args=(datos,))
        hiloVentaPorCliente = threading.Thread(target=self.procesarVentasPorCliente, args=(datos,))
   
        hiloDetallesPagos=threading.Thread(target=self.procesarDetallesPagos,args=(datos,))
        Logs.WirterTask("Hilos creados ....")
        # Iniciar la ejecución de los hilos
        
        hilo_ordenes_abiertas.start()
        hilo_punto_count.start()
        hiloVentaPorCliente.start()
      
        hiloDetallesPagos.start()
      
        Logs.WirterTask("Ya arrancaron los hilos")
        # Espera a que ambos hilos terminen su ejecución
        hilo_ordenes_abiertas.join()
        hilo_punto_count.join()
        hiloVentaPorCliente.join()
       
        hiloDetallesPagos.join()
        Logs.WirterTask("YA cunminaron los hilos ........... ")
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Precierre de Jornada</title>
        </head>
        {self.style}
        <body>
        <div>
        <p> fecha de emicion: {datetime.datetime.today()}</p>
         <center> <h1> Pre Cierre De Jornada{sede.upper()}</h1> 
          <h3> {datetime.date.today()}</h3><br/>
            <center><h2> Ventas Por clientes</h2></center>
           <table>
            <tr>
             <center> <th colspan="4">Cliente</th></center>
             <center> <th colspan="4" >Monto</th></center>
             
            </tr>
            {self.ordenesClose}
            <tr>
      <td colspan="4" class="total">Total $</td><td colspan="4" class="total">{self.totalGlobal}$</td>
  
    </tr>
          </table>
           <center><h2> Ordenenes Abiertas </h2></center>
           <table>
            <tr>
             <center> <th >#orden</th></center>
             <center> <th>cliente</th></center>
             <center> <th>total</th></center>
            <center> <th>fecha</th></center>
            <center> <th>hora</th></center>
            </tr>
            {self.OrdenesAbiertas}
          </table>
          
<center><h2> Resumen de  Pagos Percibidos </h2></center>
  


  <table>
    <tr><td colspan="5" class="total ">Total PAGO MOVIL :</td><td colspan="5" class="total ">{round(self.PAGOMOVIL,2)}$</td></tr>
    <tr><td colspan="5" class="total ">Total PUNTO DE VENTA : </td><td colspan="5" class="total">{round(self.punto,2)} $</td></tr>
    <tr><td colspan="5" class="total ">Total TRANSFERENCIAS NACIONALES :</td><td colspan="5" class="total ">{self.TRANSFERENCIANACIONAL}$</td></tr>
    <tr><td colspan="5" class="total ">Total EFECTIVO Bs:</td><td colspan="5" class="total ">{self.EFECTIVOBS}$</td></tr>
      
      <tr><td colspan="5" class="total ">Total PAY-PAL:</td><td colspan="5" class="total ">{self.totalPAYPAL}$</td></tr>
      <tr><td colspan="5" class="total ">Total ZELLE:</td><td colspan="5" class="total ">{self.totalZELLE}$</td></tr>
<tr><td colspan="5" class="total ">Total TRANSFERENCIA BANk OF AMERICA:</td><td colspan="5" class="total ">{self.TRANSFERENCIABOFA}$</td></tr>
<tr><td colspan="5" class="total ">Total BANESCO PANAMA:{self.TRANSFERENCIAPANAMA}$</td><td colspan="5" class="total ">{self.TRANSFERENCIAPANAMA}$</td></tr>
<tr><td colspan="5" class="total ">Total EFECTIVO $</td><td colspan="5" class="total ">{self.EFECTIVODIVISA}$</td></tr>
<tr><td colspan="5"class="total ">Total Wallet:</td><td colspan="5" class= "total">{self.totalWALLET}$</td></tr>
<tr><th colspan="10" class="total ">Total Bolivares:{round((self.TRANSFERENCIANACIONAL+self.PAGOMOVIL+self.punto+self.EFECTIVOBS),2)}$</th></tr>
<tr><th colspan="10" class="total ">Total Divisas:{self.TRANSFERENCIAPANAMA+self.TRANSFERENCIABOFA+self.totalZELLE+self.totalPAYPAL+self.EFECTIVODIVISA+self.totalWALLET}$</th></tr>

<tr><th colspan="10" class="total ">Total Ordenes abiertas:{self.totalOrdenesAbiertas}$</th></tr>
<tr><th colspan="10" class="total ">Total de Ventas:{self.totalGlobal+self.totalOrdenesAbiertas}$</th></tr>
<tr><th colspan="10" class="total ">Total Recibido:{self.PAGOSGLOBAL}$</th></tr>   
                             </table>
        
        
        <center>  <h2> Cierre Punto De Venta</h2></center>
          <center> <table>
            <tr>
             <center> <th >Tickets</th></center>
             <center> <th>Total</th></center>
            </tr>
            {self.puntoCount}
          </table> </center>
        </div>
        </body>
        </html>
        """
        return html
