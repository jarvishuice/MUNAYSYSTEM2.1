
import datetime
from core.Entities.ordenes.ordenesEntity import OrdenesEntity
from core.Implements.ordenes.ordenesDAO import OrdenesDao
from core.Entities.clientes.deudaClienteCoffeShopEntitity import DetalleDedudaClientesEntity
from core.Entities.ordenes.ordenesEntity import OrdenesEntity,OrdenesDetalladasEntity
from core.Entities.ordenes.detalleOrdenEntity import OrdenDetalladaEntity
from core.Entities.pedidos.pedidosEntity import PedidosEntity
from core.Entities.pagos.pagosEntity import PagosEntity
from core.Interface.ordenes.Iordenes import IOrdenes
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.ordenesDataTest.ordenesValidation import validationOrdenesData
import time
from core.Implements.pedidos.pedidosEspaciosDAO import PedidosEspaciosDAO
from core.Implements.wallet.walletDAO import WalletDAO
from core.Implements.pagos.pagosWalletDAO import PagosWalletDAO
from config.Logs.LogsActivity import Logs
from config.helpers.override import override
class OrdenesEspaciosDAO(IOrdenes,ConectionsPsqlInterface):
    validacion=validationOrdenesData()
    pedidos=PedidosEspaciosDAO()
    walletDao=WalletDAO()
    pagoWallet=PagosWalletDAO()
    def __init__(self):
        super().__init__()
    @override
    def crearOrden(self,orden: OrdenesEntity,pedido=list[PedidosEntity]) -> OrdenesEntity:
        """
        Creates a new order in the database.

        Args:
            orden (OrdenesEntity): An object representing the order to be created.
            pedido (list[PedidosEntity]): A list of objects representing the items in the order.

        Returns:
            OrdenesEntity: An object representing the created order.

        @Raises:
            INTEGRIDAD_ERROR: If there is an integrity error in the database.
            INTERFACE_ERROR: If there is an interface error in the database.
            DATABASE_ERROR: If there is an error in the database.

        Example:
            orden = OrdenesEntity(...)
            pedido = [PedidosEntity(...), PedidosEntity(...)]
            dao = OrdenesEspaciosDAO()
            result = dao.crearOrden(orden, pedido)
        """
        try:
            orden.id=time.time()
            conection= self.connect()
          
            
              
            if conection['status']==True:
                
                Logs.WirterTask(f"{self.NOTE}orden cargada como cargo a cuenyta ")
                   
                with self.conn.cursor() as cur :
                    cur.execute(f"""insert into ordenes_espacios(id,total,sede,fechapedido,fechapago,status,idcliente,idpago)
               values('{orden.id}',{orden.total},'{orden.sede}',now(),now(),'{orden.status}','{orden.idCliente}','{orden.idPago}')
                """)
                self.conn.commit()
                
                for i  in pedido:
                    i.idOrden=orden.id
                '''_var wpedidos es witerPedidos es el encargado de escribir la lista de pedidos'''
                wPedidos=self.pedidos.regVariosPedido(pedido,orden.sede)
              
                    
                return ResponseInternal.responseInternal(True,f"Orden_espacios creada de manera exitosa con el id:[{orden.id}]",orden)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    @override
    def OrdenesPorPagarBysede(self,sede: str) -> list[OrdenesEntity]:
        """
        Retrieves a list of orders that are pending payment for a specific location.

        Args:
            sede (str): The name of the location for which to retrieve the orders.

        Returns:
            list[OrdenesEntity]: A list of OrdenesEntity objects representing the orders that are pending payment for the specified location.
        
        Raises:
            INTEGRIDAD_ERROR: If there is an integrity error in the database.
            INTERFACE_ERROR: If there is an interface error in the database.
            DATABASE_ERROR: If there is an error in the database.

        """
        try:
            data=[]
            conection= self.connect()
            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""select * from ordenes_espacios where status='por pagar' and sede='{sede}' order by fechapedido desc""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(OrdenesEntity(id=str(i[0]),total=float(i[1]),sede=str(i[2]),fechapedido=str(i[3]),status=str(i[5]),idCliente=int(i[6])))     
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) en la sede {sede}",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}:No se encontraron ordenes por pagar ",data)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    @override
    def OrdenesFilterByStatusAndSede(self,status:None or any or str, sede:str or any or None) -> list[OrdenesEntity | None]:
        """
        Retrieves a list of orders that match a specific status and location.

        Args:
            status (str): The status of the orders to retrieve. It can be any string value.
            sede (str): The location of the orders to retrieve. It must be a valid string value.

        Returns:
            list[OrdenesEntity | None]: A list of OrdenesEntity objects representing the orders that match the specified status and sede.
        """
        try:
          conection= self.connect()  
          data=[]
          validacionSede=self.validacion.validarSede(sede)
          validacionStatus=self.validacion.validarStatus(status)               
          if validacionSede==False and validacionStatus ==False:
            Logs.WirterTask(f"""{self.NOTE} error en la validacion de status and sede de las ordenesdetail({status,sede})""")
            return ResponseInternal.responseInternal(False,"error en la validacion de status and sede ",[]) 
          else:
            
          
            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""select * from ordenes_espacios where status='{status}' and sede='{sede}' order by fechapedido desc""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(OrdenesEntity(id=str(i[0]),total=float(i[1]),sede=str(i[2]),fechaPedido=str(i[3]),status=str(i[5]),idCliente=int(i[6])))     
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) en la sede {sede}",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}:No se encontraron ordenes por pagar ",data)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    @override
    def OrdenesAbiertasByClienteAndSede(self,idCliente: int, sede: str) -> list[OrdenesEntity]:
        """
        Retrieves open orders for a specific client and location.

        Args:
            idCliente (int): The ID of the client for whom to retrieve the orders.
            sede (str): The location (sede) for which to retrieve the orders.

        Returns:
            list[OrdenesEntity]: A list of OrdenesEntity objects representing the open orders for the specified client and location.
        """
        try:
            conection= self.connect()  
            data=[]

            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""select * from ordenes_espacios where idcliente={idCliente} and sede ='sede' and status ='por pagar'""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(OrdenesEntity(id=str(i[0]),total=float(i[1]),sede=str(i[2]),fechaPedido=str(i[3]),status=str(i[5]),idCliente=int(i[6])))     
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) ordenes  en la sede {sede} del cliente  ({idCliente}).....!" ,data)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}:No se encontraron ordenes por pagar  del cliente ",data)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
            Logs.WirterTask("Finalizada la busqueda de ordenes del cliente {idCliente}")
            
    @override
    def OrdenesDeLajornada(self,sede: str) -> list[OrdenesEntity]:
        """
        Este método obtiene las órdenes del día de una base de datos para una ubicación específica.

        Args:
         sede (str): La ubicación para la cual obtener las órdenes.

        Returns:
         list[OrdenesEntity]: Una lista de objetos OrdenesEntity que representan las órdenes del día.
        """
        data=[]
        try:
            conexion=self.connect()
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                    cur.execute(f"""
                           select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora  , o.status from ordenes_espacios o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and o.sede='{sede}' and date(o.fechapedido)='{str(datetime.date.today())}'
order by o.id desc 
                                """);
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(OrdenesDetalladasEntity(idOrden=str(i[0]),
                                                  cliente=str(i[1]),
                                                  total=float(i[2]),
                                                  fecha=str(i[3]),
                                                  hora=str(i[4]),
                                                  status=str(i[5])
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
   
    @override
    def getDetailOrden(self,idOrden:str) -> list[OrdenDetalladaEntity]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                        select i.nombre ,p.cantidad,i.precio,p.total from pedidos_espacios p 
                        inner join productos_espacios i on i.precio=i.precio and i.nombre=i.nombre
                        inner join ordenes o on o.fechapedido =o.fechapedido 
                        where o.id = '{idOrden}' and i.id=p.idproducto and p.idorden ='{idOrden}' 
                                """);        
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(OrdenDetalladaEntity(nombre=str(i[0]),
                                                  cantidad=float(i[1]),
                                                  precio=float(i[2]),
                                                  total=float(i[3]),
                                                  
                                                 ))     
                        return  ResponseInternal.responseInternal(True,f"Ordnees_espacios del dia abiertas extraidas con exito",data)
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
    @override        
    def getOrdenesBysede(self,sede: str) -> list[OrdenesDetalladasEntity | None]:
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                        select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora  , o.status from ordenes_espacios o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and o.sede='{sede}' and o.status = 'por pagar'  order  by o.fechapedido desc 
                                """);
              
             
        
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(OrdenesDetalladasEntity(idOrden=str(i[0]),
                                                  cliente=str(i[1]),
                                                  total=float(i[2]),
                                                  fecha=str(i[3]),
                                                  hora=str(i[4]),
                                                  status=str(i[5])
                                                  
                                                 ))     
                        return  ResponseInternal.responseInternal(True,f"ordenes de la sede {sede} extraida con exito ",data)
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
            Logs.WirterTask("Finalida la lectura de las ordenes de la sede {sede}")
            self.disconnect() 
    @override
    def deleteOrder(self,idOrden: str) -> bool:
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""delete from pedidos_espacios where idorden='{idOrden}';
                       delete from ordenes_espacios where id='{idOrden}';""");
              
                    self.conn.commit()    
        
                    count= cur.rowcount
                    if count > 0 :
                          
                        return  ResponseInternal.responseInternal(True,f"la orden {idOrden}  fue eliminada con exito",True)
                    else:
                        Logs.WirterTask(f"{self.NOTE } se leyeron las ordnes pero on encontramos ninguna  ")
                        return ResponseInternal.responseInternal(True, "{self.NOTE} No se pudo eliminrar la orden {idOrden} probablkemente no exite ...  ",True)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalida la lectura de las ordenes de la sede {sede}")
            self.disconnect()                     