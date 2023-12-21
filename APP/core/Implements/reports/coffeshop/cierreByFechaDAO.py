import datetime
from core.Entities.reports.coffeshop.cofeshopReportEntity import DetallesPedidos, DeudaCliente, ReporteCoffeshopEntity,DetallePagos, OrdenesAbiertas, PuntoCount, VentasPorClientes, VentasPorProducto, WalletDisponibles
from core.Interface.reports.coffeshop.ICIerreReportByFecha import ICierreByFecha

from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
from core.utils.plantellaHTMLCIERREByFecha import PlantillaHTMLCierreJornada
import pdfkit

import time

from config.Logs.LogsActivity import Logs
class ReportCierreByFechaDAO(ConectionsPsqlInterface,ICierreByFecha):
    validacion=validationPedidosData()
    plantilla=PlantillaHTMLCierreJornada()
    OPTIONS = {
                      'page-size': 'Letter', 
      'margin-top': '0.75in',
      'margin-right': '0.75in',
      'margin-bottom': '0.75in', 
      'margin-left': '0.75in'
                    }
    def __init__(self):
        super().__init__()
    def __VentasClientes__(self,sede:str,ano:int,mes:int,day:int) -> list[VentasPorClientes]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          select sum(total),c.nombre from ordenes o
inner join clientes c on c.nombre=c.nombre 
where c.id=idcliente  and status= 'pagado' and  sede='{sede}' and date(o.fechapedido)= ' {ano}-{mes}-{day} ' 
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
            
        
    def __OrdenesAbiertas__(self,sede:str,ano:int,mes:int,day:int) -> list[OrdenesAbiertas]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora from ordenes o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and status= 'por pagar' and sede='{sede}' and date(o.fechapedido)='{ano}-{mes}-{day}'
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
                        Logs.WirterTask(f"{self.NOTE } se leyeron las ordnes pero on encontramos ninguna  ")
                        return ResponseInternal.responseInternal(True, "{self.NOTE} Las ordnes se leyeron de manera correctapero no conseguimos nada ...  ",data)
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
           
    def __DetallesPagos__(self,sede:str,ano:int,mes:int,day:int) -> list[DetallePagos]:
       
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
and date(p.fechapago) =' {ano}-{mes}-{day} ' and monto > 0 and f.id=p.idformadepago and t.id=p.idtaza     
              
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
            
    def __countPunto__(self,sede:str,ano:int,mes:int,day:int) -> list[PuntoCount]:

       
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
inner join tazadollar t on precio=precio where idformadepago ={selector} AND motivo ilike '%{sede}%' AND date(p.fechapago) ='{ano}-{mes}-{day}' and t.id = p.idtaza ;
                             
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
            
            
            
    def __ventasPorProducto__(self,sede:str,ano:int,mes:int,day:int) -> list[VentasPorProducto]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          SELECT SUM(p.cantidad) AS cantidad, SUM(p.total) AS monto, i.nombre
FROM pedidos p
INNER JOIN inventario{sede} i ON i.id = i.id
INNER JOIN ordenes o ON p.idorden = o.id
WHERE DATE(o.fechapedido) = '{ano}-{mes}-{day}'
    AND o.sede = '{sede}'
    and i.id=idproducto
GROUP BY i.nombre;
                                """);       
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(VentasPorProducto(producto=str(i[2]),
                                                cantidad=float(i[0]),
                                                total=float(i[1])))     
                        return  ResponseInternal.responseInternal(True,f"lectura de ventas por productos diarias realizado con exito",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer vnetas por producto  ")
                        return ResponseInternal.responseInternal(False, "error al leer las ventas por producto  ",None)
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
    def __DeudaCleinteBysede__(self,sede:str,ano:int,mes:int,day:int) -> list[DeudaCliente]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          SELECT c.nombre, SUM(o.total) 
FROM ordenes o
INNER JOIN clientes c ON o.idcliente = c.id
WHERE o.sede = '{sede}' AND o.status = 'por pagar'
GROUP BY c.nombre
order by c.nombre ;
                                """);       
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(DeudaCliente(cliente=str(i[0]),
                                                deuda=float(i[1])))     
                        return  ResponseInternal.responseInternal(True,f"lectura de deudas clientes r realizada de maenra satisfactoria ",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer deudas de clientes  ")
                        return ResponseInternal.responseInternal(False, "error al leer Ordenes historicas  ",None)
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
    def __DetallesPedidos__(self,sede:str,ano:int,mes:int,day:int) -> list[DetallesPedidos]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select idorden,c.nombre,p3.nombre ,p2.cantidad,p2.total,date(o.fechapedido) as fecha,to_char(o.fechapedido ,'hh12:MI:SS AM') as hora from pedidos p2 
left join productos  p3 on nombre=p3.nombre 
left join clientes c on c.nombre=c.nombre
left join ordenes o  on o.id =o.id
where  p3.id = idproducto and c.id=o.idcliente  and o.id=p2.idorden  and date(o.fechapedido) ='{ano}-{mes}-{day}' and o.sede='{sede}';      
              
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(DetallesPedidos(
                                                  idOrden=str(i[0]),
                                                  cliente=str(i[1]),
                                                  producto=str(i[2]),
                                                  cantidad=float(i[3]),
                                                  total=float(i[4]),
                                                  fecha=str(i[5]),
                                                  hora=str(i[6]),
                                                ))     
                        return  ResponseInternal.responseInternal(True,f" detalles de pedidos extraidos de manera correcta ",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } errror al extraer los pedidos del dia   ")
                        return ResponseInternal.responseInternal(False, "error al extraer los pedidos del dia  ",None)
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
    def __OrdenesHistoricas__(self,sede:str,ano:int,mes:int,day:int) -> list[OrdenesAbiertas]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora from ordenes o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and status= 'por pagar' and sede='{sede}' and date(o.fechapedido)<> '{ano}-{mes}-{day}';
                                """);       
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(OrdenesAbiertas(idOrden=str(i[0]),
                                                cliente=str(i[1]),
                                                total=float(i[2]),
                                                fecha=str(i[3]),
                                                hora=str(i[4])))     
                        return  ResponseInternal.responseInternal(True,f"lectura de ordenes por pagar historicas realizada de maenra satisfactoria ",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer ordnees historicas por pagar core reportes  ")
                        return ResponseInternal.responseInternal(True, "{self.NOTE} Las ordnes se leyeron de manera correctapero no conseguimos nada ...  ",data)
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

    def __walletDisponible__(self,sede:str) -> list[WalletDisponibles]:
        try:
            data=[]          
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           SELECT  idcliente, nombre,SUM(monto) AS total
FROM wallet w  
inner join clientes c on nombre=c.nombre
where c.id=w.idcliente 
GROUP BY w.idcliente,c.nombre  
HAVING SUM(monto) > 0;
              
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(WalletDisponibles(
                                                  idCliente=int(i[0]),
                                                  cliente=str(i[1]),
                                                  total=str(i[2]),
                                                  
                                                ))     
                        return  ResponseInternal.responseInternal(True,f" detalles de wallet disponibles extraidos con exito ",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } errror al extraer los wallets disponibles    ")
                        return ResponseInternal.responseInternal(False, "error al extraer los wallets disponibles   ",None)
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
    def generarCierre(self,sede:str,ano:int,mes:int,day:int):
        try:
            ventaCLientes=[]
            detallePago=[]
            ventaCLientes=self.__VentasClientes__(sede,ano,mes,day)['response']
            detallePago=self.__DetallesPagos__(sede,ano,mes,day)['response']
            #Logs.WirterTask(type(self.__VentasClientes__(sede,ano,mes,day)['response'][1]))
            print(type(self.__VentasClientes__(sede,ano,mes,day)['response']))
            html=''
            output_path =f"assets/reports/coffeshop/cierre/CierreDeJornada{sede}{datetime.datetime.today()}.pdf"
            print(type(self.__VentasClientes__(sede,ano,mes,day)['response']))
            
            datos=ReporteCoffeshopEntity(ventasPorProductos=self.__ventasPorProducto__(sede,ano,mes,day)['response'],deudaCliente=self.__DeudaCleinteBysede__(sede,ano,mes,day)['response'],detallePedidos=self.__DetallesPedidos__(sede,ano,mes,day)['response'],walletDisponibles=self.__walletDisponible__(sede)['response'],ventasPorCliente=ventaCLientes,ordenesAbiertasHistoricas=self.__OrdenesHistoricas__(sede,ano,mes,day)['response'],ordenesAbiertas=self.__OrdenesAbiertas__(sede,ano,mes,day)['response'],detallePagos=detallePago,puntoCount=self.__countPunto__(sede,ano,mes,day)['response'])
            
                
            print(type(self.__VentasClientes__(sede,ano,mes,day)['response']))
            html=self.plantilla.getHTML(datos,sede,ano,mes,day)
            pdf=pdfkit.from_string(html,output_path,options=self.OPTIONS)
            return ResponseInternal.responseInternal(True,"reporte de inventario generado con exito",output_path)
                
                
            
            
        finally:        
                Logs.WirterTask(f"finalizado el reporte de inventario de la sede {sede}")