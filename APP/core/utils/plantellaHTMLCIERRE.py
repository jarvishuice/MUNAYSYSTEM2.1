import threading
from core.Entities.reports.coffeshop.cofeshopReportEntity import ReporteCoffeshopEntity
import datetime
from config.Logs.LogsActivity import Logs

class PlantillaHTMLCierreJornada():
    def __init__(self):
        pass
    def procesarVentasProductos(self,datos:ReporteCoffeshopEntity):
        self.ventasProductos=''
        self.totalventasProductos=0
        if datos.ventasPorProductos is not None:
           for i in datos.ventasPorProductos:
                
            self.ventasProductos+=f"""<tr> <td colspan=3>{i.producto} </td><td>{i.cantidad} </td> <td>{i.total}</td></tr>"""
            self.totalventasProductos+=i.total
    def procesarDeudaClientes(self,datos:ReporteCoffeshopEntity):
        self.deudaCleintes=''
        self.totalDeudasClientes=0
        if datos.deudaCliente is not None:
          for i in datos.deudaCliente:  
            self.deudaCleintes +=f"""<tr> <td>{i.cliente}</td> <td>{i.deuda}</td></tr>"""
            self.totalDeudasClientes += i.deuda
    def procesarDetallesOrdenestoday(self,datos:ReporteCoffeshopEntity):
        self.detalleOrdenes=''
        self.totalDetalleOrdenes=0
        if datos.detallePedidos is not None:
            for i in datos.detallePedidos:
                self.detalleOrdenes+=f"""<tr><td>{i.idOrden}</td><td>{i.cliente}</td><td>{i.producto}</td><td>{i.cantidad}</td> <td>{i.total/i.cantidad}</td> <td>{i.total}</td><td>{i.fecha}</td><td>{i.hora}</td></tr>"""
                self.totalDetalleOrdenes+=i.total 
    def procesarWalletsActivos(self,datos:ReporteCoffeshopEntity):
        self.totalWalletActivos=0
        self.walletActivos=''
        if datos.walletDisponibles is not None:
            for i in datos.walletDisponibles:
                self.walletActivos += f""" <tr> <td>{i.idCliente} </td><td > {i.cliente}</td> <td> {i.total}</td></tr>"""
                self.totalWalletActivos += i.total
    def procesarOrdenesAbiertasHistoricas(self,datos:ReporteCoffeshopEntity):
        self.OrdenesAbiertasHistoricas=''
        self.totalOrdenesAbiertasHistoricas=0
        if len(datos.ordenesAbiertasHistoricas) > 0:
            for i in datos.ordenesAbiertasHistoricas:
                self.OrdenesAbiertasHistoricas+=f"""<tr> <td>{i.idOrden}</td><td>{i.cliente}</td><td>{i.total}$ </td> <td>{i.fecha}<td> {i.hora}</td></tr>"""
                self.totalOrdenesAbiertasHistoricas += i.total
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
        if datos.ordenesAbiertas is not None:
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
            self.pagos+=f"""<tr><td>{i.cliente}</td><td>{i.monto} $</td><td>{round((i.monto) * (i.cotizacion),2)} bs</td><td>{i.cotizacion}</td><td>{i.motivo}</td><td>{i.metodo}</td> <td>{i.banco}</td><td>{i.referencia}</td></tr>"""
            
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
               
                  self.totalWALLET += i.monto
              
      
      
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
        hiloWalletsActivos=threading.Thread(target=self.procesarWalletsActivos,args=(datos,))
        hiloordenesHistoricas=threading.Thread(target=self.procesarOrdenesAbiertasHistoricas,args=(datos,))
        hiloDetallesPagos=threading.Thread(target=self.procesarDetallesPagos,args=(datos,))
        hiloDetalleOrdenes=threading.Thread(target=self.procesarDetallesOrdenestoday,args=(datos,))
        hilodeudaCleintes=threading.Thread(target=self.procesarDeudaClientes,args=(datos,))
        hiloVentaProductos=threading.Thread(target=self.procesarVentasProductos,args=(datos,))
        Logs.WirterTask("Hilos creados ....")
        # Iniciar la ejecución de los hilos
        
        hilo_ordenes_abiertas.start()
        hilo_punto_count.start()
        hiloVentaPorCliente.start()
        hiloWalletsActivos.start()
        hiloordenesHistoricas.start()
        hiloDetallesPagos.start()
        hiloDetalleOrdenes.start()
        hilodeudaCleintes.start()
        hiloVentaProductos.start()
           
        Logs.WirterTask("Ya arrancaron los hilos")
        # Espera a que ambos hilos terminen su ejecución
        hilo_ordenes_abiertas.join()
        hilo_punto_count.join()
        hiloVentaPorCliente.join()
        hiloWalletsActivos.join()
        hiloordenesHistoricas.join()
        hiloDetallesPagos.join()
        hiloDetalleOrdenes.join()
        hilodeudaCleintes.join()
        hiloVentaProductos.join()
        Logs.WirterTask("YA cunminaron los hilos ........... ")
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Reporte del Fin de Jornada</title>
        </head>
        {self.style}
        <body>
        <div>
        <p> fecha de emicion: {datetime.datetime.today()}</p>
         <center> <h1> Reporte del Fin de Jornada {sede.upper()}</h1> 
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
          
           <center><h2> Ventas Por Productos</h2></center>
           <table>
            <tr>
             <center> <th colspan="3">Nombre</th></center>
             <center> <th>Cantidad</th></center>
             <center> <th>Monto$</th></center>
             
            </tr>
            {self.ventasProductos}
            <tr>
      <td colspan="4" class="total">Total $</td><td colspan="4" class="total">{self.totalventasProductos}$</td>
  
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
          
          <center><h2> Detalle de Ordenes de la Jornada </h2></center>
  


  <table>
    <tr>
     <center> <th>#Orden</th></center>
     <center> <th>Cliente</th></center>
     <center> <th>Producto</th></center>
      <th>Cantidad</th>
      <th>Precio</th>
      <th>Total$</th>
      <th>Fecha </th>
      <th>Hora</th>

      


    </tr>
    {self.detalleOrdenes}
    <tr><td class ='total' colspan=5> total </td><td class='total'>{self.totalDetalleOrdenes}</td> </tr>
      
      </table>
          
          
          
   <center><h2> Pagos Percibidos en la Jornada </h2></center>
  


  <table>
    <tr>
     <center> <th>Cliente</th></center>
     <center> <th>Monto $</th></center>
     <center> <th>Monto Bs</center>
     <center> <th>Taza </th></center>
     <center> <th>Motivo</th></center>
     <th>Metodo</th>
     <th>Banco</th>
      <th>Referencia</th>
    </tr>
    {self.pagos}
    <tr> <td class='total'> Total</td> <td class='total'>{self.PAGOSGLOBAL}</td></tr>
    </table>
    </br>       
          
          
          
          
<center><h2> Totales  De Formas De Pago </h2></center>
  


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
          
          <center><h2>Walet Activos </h2></center> 
    <table>
    <tr>
     <center> <th>id</th></center>
     <center> <th>nombre </th></center>
     <center> <th>Monto $</center>
    
    </tr>
    {self.walletActivos}
    <tr> <td colspan=2 class='total'> total:</td> <td class ='total'>{self.totalWalletActivos}$</td></tr>
 </table>
 
           <center><h2> Deudas Clientes </h2></center>
           <table>
            <tr>
             <center> <th >Cliente</th></center>
             <center> <th>total</th></center>
             
            </tr>
            {self.deudaCleintes}
           <tr><td  class='total'>total:</td> <td class='total'>{self.totalDeudasClientes}$</td> </tr>
          </table> 
          
        </div>
        </body>
        </html>
        """
        return html
