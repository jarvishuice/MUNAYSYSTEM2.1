import datetime
from core.Entities.reports.coffeshop.cofeshopReportEntity import ReporteCoffeshopEntity,DetallePagos, OrdenesAbiertas, PuntoCount, VentasPorClientes
from core.Interface.reports.coffeshop.IPrecierreReport import IPrecierre

from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
from core.utils.plantillaHTMLPreCierreJornada import PlantillaHTMLPreCierreJornada
import pdfkit

import time

from config.Logs.LogsActivity import Logs
class ReportPreCierreDAO(ConectionsPsqlInterface,IPrecierre):
    validacion=validationPedidosData()
    plantilla=PlantillaHTMLPreCierreJornada()
    OPTIONS = {
                      'page-size': 'Letter', 
      'margin-top': '0.75in',
      'margin-right': '0.75in',
      'margin-bottom': '0.75in', 
      'margin-left': '0.75in'
                    }
    def __init__(self):
        super().__init__()
    def __VentasClientes__(self,sede: str) -> list[VentasPorClientes]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          select sum(total),c.nombre from ordenes o
inner join clientes c on c.nombre=c.nombre 
where c.id=idcliente  and status= 'pagado' and  sede='{sede}' and date(o.fechapedido)= ' {datetime.date.today()} ' 
group  by c.nombre
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(VentasPorClientes(total=float(i[0]),
                                                  cliente=str(i[1])
                                                 
                                                 ))     
                        return  ResponseInternal.responseInternal(True,f"Ordnees del dia abiertas extraidas con exito",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer el inventario ")
                        return ResponseInternal.responseInternal(False, "error al intentar registrar el producto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()
            
        
    def __OrdenesAbiertas__(self,sede: str) -> list[OrdenesAbiertas]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora from ordenes o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and status= 'por pagar' and sede='{sede}' and date(o.fechapedido)='{datetime.date.today()}'
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(OrdenesAbiertas(idOrden=str(i[0]),
                                                  cliente=str(i[1]),
                                                  total=float(i[2]),
                                                  fecha=str(i[3]),
                                                  hora=str(i[4]),
                                                 ))     
                        return  ResponseInternal.responseInternal(True,f"Ordnees del dia abiertas extraidas con exito",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer las ordenes ")
                        return ResponseInternal.responseInternal(False, "error al intentar registrar el producto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()
           
    def __DetallesPagos__(self,sede: str) -> list[DetallePagos]:
       
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select nombre,monto,precio,motivo, referencia,date(p.fechapago) as fecha,to_char(p.fechapago  ,'hh12:MI:SS AM') as hora,banco,metodo from pagos p 
inner join clientes c on nombre=c.nombre
inner join fromadepago f on banco=f.banco and metodo=f.metodo
inner join tazadollar t ON precio=t.precio 
where c.id=p.idcliente and motivo ILIKE '%{sede}%'
and date(p.fechapago) =' {datetime.date.today()} ' and monto > 0 and f.id=p.idformadepago and t.id=p.idtaza     
              
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(DetallePagos(cliente=str(i[0]),
                                                  monto=float(i[1]),
                                                  cotizacion=float(i[2]),
                                                  motivo=str(i[3]),
                                                  referencia=str(i[4]),
                                                  fecha=str(i[5]),
                                                  hora=str(i[6]),
                                                  banco=str(i[7]),
                                                  metodo=str(i[8])))     
                        return  ResponseInternal.responseInternal(True,f"Pagos extraida de manera correcta",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } werrror al leeer los pagos de l dia  ")
                        return ResponseInternal.responseInternal(False, "error al intentar registrar el producto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()
            
    def __countPunto__(self,sede: str) -> list[PuntoCount]:

       
        data=[]
        try:
            conexion=self.connect()
            selector=None
            if sede == 'jalisco':
                selector=6
            else:
                selector = 15
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select coalesce(count(monto),0),coalesce(sum(monto * precio),0) from pagos as p 
inner join tazadollar t on precio=precio where idformadepago ={selector} AND motivo ilike '%{sede}%' AND date(p.fechapago) =' {datetime.date.today()} ' and t.id = p.idtaza ;
                             
                                """);       
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(PuntoCount(cantidad=int(i[0]),
                                                monto=float(i[1])))     
                        return  ResponseInternal.responseInternal(True,f"registro de pruntos  extraidos de manera correcta de manera correcta",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer el punto ")
                        return ResponseInternal.responseInternal(False, "error al leer el punto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()        
            
            
            
            
            
    def generarPrecierre(self,sede: str):
        try:
            ventaCLientes=[]
            detallePago=[]
            ventaCLientes=self.__VentasClientes__(sede)['response']
            detallePago=self.__DetallesPagos__(sede)['response']
            #Logs.WirterTask(type(self.__VentasClientes__(sede)['response'][1]))
            print(type(self.__VentasClientes__(sede)['response']))
            html=''
            output_path =f"assets/reports/coffeshop/precierre/precierre{sede}{datetime.datetime.today()}.pdf"
            print(type(self.__VentasClientes__(sede)['response']))
            
            datos=ReporteCoffeshopEntity(ventasPorCliente=ventaCLientes, ordenesAbiertas=self.__OrdenesAbiertas__(sede)['response'],detallePagos=detallePago,puntoCount=self.__countPunto__(sede)['response'])
            
                
            print(type(self.__VentasClientes__(sede)['response']))
            html=self.plantilla.getHTML(datos,sede)
            pdf=pdfkit.from_string(html,output_path,options=self.OPTIONS)
            return ResponseInternal.responseInternal(True,"reporte de inventario generado con exito",output_path)
                
                
            
            
        finally:        
                Logs.WirterTask(f"finalizado el reporte de inventario de la sede {sede}")