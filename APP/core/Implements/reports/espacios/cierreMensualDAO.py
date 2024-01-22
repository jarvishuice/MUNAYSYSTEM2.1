import datetime
from core.Entities.reports.espacios.reporteEspaciosEntity import DetallesPedidos, DeudaCliente, ReporteEspaciosEntity,DetallePagos, OrdenesAbiertas, PuntoCount, VentasPorClientes, VentasPorProducto, WalletDisponibles
from core.Interface.reports.coffeshop.ICierreReport import ICierre

from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
#from core.utils.plantellaHTMLCIERRE import PlantillaHTMLCierreJornada
from core.utils.plantillaHtmlMEnsualEspacios import PlantillaHTMLMensual
import pdfkit

import time

from config.Logs.LogsActivity import Logs
class ReportCierreMensualDAO(ConectionsPsqlInterface,ICierre):
    validacion=validationPedidosData()
    plantilla=PlantillaHTMLMensual()
    OPTIONS = {
                      'page-size': 'Letter', 
      'margin-top': '0.75in',
      'margin-right': '0.75in',
      'margin-bottom': '0.75in', 
      'margin-left': '0.75in'
                    }
    def __init__(self):
        super().__init__()
    def __VentasClientes__(self,sede: str,mes:int,year:int) -> list[VentasPorClientes]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                        SELECT SUM(total), c.nombre 
FROM ordenes_espacios o
INNER JOIN clientes c ON c.id = o.idcliente
WHERE status = 'pagado' AND sede = '{sede}' AND EXTRACT(MONTH FROM o.fechapedido) = {mes} AND EXTRACT(YEAR FROM o.fechapedido) = {year}
GROUP BY c.nombre;      """);
              
             
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
            
        
    def __OrdenesAbiertas__(self,sede: str, mes:int,year:int) -> list[OrdenesAbiertas]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                        SELECT o.id, c.nombre, total, DATE(o.fechapedido) AS fecha, TO_CHAR(o.fechapedido, 'HH12:MI:SS AM') AS hora 
FROM ordenes_espacios o
INNER JOIN clientes c ON c.id = o.idcliente
WHERE status = 'por pagar' AND sede = '{sede}' AND EXTRACT(MONTH FROM o.fechapedido) = {mes} AND EXTRACT(YEAR FROM o.fechapedido) = {year}

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
           
    def __DetallesPagos__(self,sede: str,mes:int,year:int) -> list[DetallePagos]:
       
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                       SELECT 
    nombre,
    monto,
    precio,
    motivo,
    referencia,
    date(p.fechapago) AS fecha,
    to_char(p.fechapago, 'hh12:MI:SS AM') AS hora,
    banco,
    metodo 
FROM 
    pagos_espacios p 
INNER JOIN 
    clientes c ON nombre=c.nombre
INNER JOIN 
    fromadepago f ON banco=f.banco AND metodo=f.metodo
INNER JOIN 
    tazadollar t ON precio=t.precio 
WHERE 
    c.id=p.idcliente AND 
    p.sede = '{sede}' AND 
    EXTRACT(YEAR FROM p.fechapago) = {year} AND 
    EXTRACT(MONTH FROM p.fechapago) = {mes} AND 
    monto > 0 AND 
    f.id=p.idformadepago AND 
    t.id=p.idtaza;
   
              
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
            
    def __countPunto__(self,sede: str, mes:int,year:int) -> list[PuntoCount]:

       
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
                    SELECT 
    COALESCE(COUNT(monto), 0),
    COALESCE(SUM(monto * precio), 0) 
FROM 
    pagos_espacios AS p 
INNER JOIN 
    tazadollar t ON precio=precio 
WHERE 
    idformadepago = {selector} AND 
    sede = '{sede}' AND 
    EXTRACT(YEAR FROM p.fechapago) = {year} AND 
    EXTRACT(MONTH FROM p.fechapago) = {mes} AND 
    t.id = p.idtaza;
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
            
            
            
    def __ventasPorProducto__(self,sede: str,mes:int,year:int) -> list[VentasPorProducto]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                       SELECT 
    SUM(p.cantidad) AS cantidad, 
    SUM(p.total) AS monto, 
    i.nombre
FROM 
    pedidos_espacios p
INNER JOIN 
    productos_espacios i ON i.id = i.id
INNER JOIN 
    ordenes_espacios o ON p.idorden = o.id
WHERE 
    EXTRACT(YEAR FROM o.fechapedido) = {year} AND 
    EXTRACT(MONTH FROM o.fechapedido) = {mes} AND 
    o.sede = '{sede}' AND 
    i.id=idproducto
GROUP BY 
    i.nombre;

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
    def __DeudaCleinteBysede__(self,sede: str) -> list[DeudaCliente]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          SELECT c.nombre, SUM(o.total) 
FROM ordenes_espacios o
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
    def __DetallesPedidos__(self,sede: str,mes:int,year:int) -> list[DetallesPedidos]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                          SELECT 
    idorden,
    c.nombre,
    p3.nombre,
    p2.cantidad,
    p2.total,
    date(o.fechapedido) AS fecha,
    to_char(o.fechapedido, 'hh12:MI:SS AM') AS hora 
FROM 
    pedidos_espacios p2 
LEFT JOIN 
    productos_espacios p3 ON nombre=p3.nombre 
LEFT JOIN 
    clientes c ON c.nombre=c.nombre
LEFT JOIN 
    ordenes_espacios o ON o.id =o.id
WHERE  
    p3.id = idproducto AND 
    c.id=o.idcliente AND 
    o.id=p2.idorden AND 
    EXTRACT(YEAR FROM o.fechapedido) = {year} AND 
    EXTRACT(MONTH FROM o.fechapedido) = {mes} AND 
    o.sede='{sede}';

              
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
    def __OrdenesHistoricas__(self,sede: str) -> list[OrdenesAbiertas]:
        data=[]
        try:
            conexion=self.connect()
           
          
            
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora from ordenes_espacios o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and status= 'por pagar' and sede='{sede}' and date(o.fechapedido)<> '{datetime.date.today()}';
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

    def __walletDisponible__(self,sede: str) -> list[WalletDisponibles]:
        try:
            data=[]          
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           SELECT  idcliente, nombre,SUM(monto) AS total
FROM wallet_espacios w  
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
    def generarCierre(self,sede: str,mes:int,year:int):
        try:
            ventaCLientes=[]
            detallePago=[]
            ventaCLientes=self.__VentasClientes__(sede,mes,year)['response']
            detallePago=self.__DetallesPagos__(sede,mes,year)['response']
            #Logs.WirterTask(type(self.__VentasClientes__(sede)['response'][1]))
            print(type(self.__VentasClientes__(sede,mes,year)['response']))
            html=''
            output_path =f"assets/reports/espacios/mensual/CierreMensual{sede}{datetime.datetime.today()}.pdf"
            print(type(self.__VentasClientes__(sede,mes,year)['response']))
            
            datos=ReporteEspaciosEntity(ventasPorProductos=self.__ventasPorProducto__(sede,mes,year)['response'],deudaCliente=self.__DeudaCleinteBysede__(sede)['response'],detallePedidos=self.__DetallesPedidos__(sede,mes,year)['response'],walletDisponibles=self.__walletDisponible__(sede)['response'],ventasPorCliente=ventaCLientes,ordenesAbiertasHistoricas=self.__OrdenesHistoricas__(sede)['response'],ordenesAbiertas=self.__OrdenesAbiertas__(sede,mes,year)['response'],detallePagos=detallePago,puntoCount=self.__countPunto__(sede,mes,year)['response'])
            
                
            print(type(self.__VentasClientes__(sede,mes,year)['response']))
            html=self.plantilla.getHTML(datos,sede,mes,year)
            pdf=pdfkit.from_string(html,output_path,options=self.OPTIONS)
            return ResponseInternal.responseInternal(True,"reporte de inventario generado con exito",output_path)
                
                
            
            
        finally:        
                Logs.WirterTask(f"finalizado el reporte de inventario de la sede {sede}")