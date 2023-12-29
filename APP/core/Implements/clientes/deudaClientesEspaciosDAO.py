from core.Entities.pagos.pagosEntity import PagosEntity
from core.Entities.clientes.deudaClienteCoffeShopEntitity import DetalleDedudaClientesEntity, DeudaClienteCoffeShopEntity 
from core.Interface.clients.IdeudaClientes import IDedudaClientes
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface

from core.Implements.pagos.pagosEspaciosDAO import PagosEspaciosDAO
from core.Implements.pagos.pagosWalletDAO import PagosWalletDAO
from core.Implements.wallet.walletDAO import WalletDAO,WalletEntity
import time
from config.Logs.LogsActivity import Logs
class DeudaCientesEspaciosDAO(ConectionsPsqlInterface,IDedudaClientes):
    def __init__(self):
        super().__init__()
    integracionPagos=PagosEspaciosDAO()
    integracionWalletPagos=PagosWalletDAO()
    integracionWallet=WalletDAO()
    def getDeudasClientesBySede(self,sede) -> list[DeudaClienteCoffeShopEntity]:
        try:
            conection= self.connect()  
            data=[]

            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""select sum (o.total) as deuda,count(o.total) as cantidad_ordenes,c.nombre,c.id,c.ci from  ordenes_espacios o
inner join clientes c on c.nombre=c.nombre and c.id=c.id and c.ci =c.ci
where o.status ='por pagar' and o.sede='{sede}' and c.id=o.idcliente  
group by c.nombre ,c.id""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(DeudaClienteCoffeShopEntity(idCliente=int(i[3]),ci=str(i[4]),nombre=str(i[2]),cantidadOrdenes=int(i[1]),deuda=float(i[0])))     
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) deudas  en la sede {sede} .....!" ,data)
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
    def getDetalleDeudaClienteBySede(self,sede:str,idCliente:int) -> list[DetalleDedudaClientesEntity]:
        try:
            conection= self.connect()  
            data=[]

            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""select o.fechaPedido,i.nombre,p.cantidad,p.total,p.idorden  from pedidos_espacios p
inner join productos_espacios i on i.nombre=i.nombre
inner join ordenes_espacios o on o.fechapedido = o.fechapedido
inner join clientes c on c.nombre =c.nombre
where o.idcliente ={idCliente} and sede='{sede}' and i.id=p.idproducto and o.id = p.idorden and o.status='por pagar' and o.idcliente = c.id
group by c.nombre ,p.idorden,i.nombre,p.cantidad,p.total,o.fechapedido;
""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(DetalleDedudaClientesEntity(fechaPedido=str(i[0]),producto=str(i[1]),cantidad=int(i[2]),precio=float(i[3]/i[2]),total=float(i[3]),sede=str(sede),idOrden=str(i[4])))     
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) de pedidos  en la sede {sede} del cliente {idCliente} .....!" ,data)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}:No se encontraron deudas del cliente {idCliente} en la sede {sede} ",data)
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
    def closeDeudaClientBySede(self,pago: PagosEntity, Rwallet: float,Dwallet: float) -> PagosEntity:
    
        try:
            conexion= self.connect()
            if conexion['status'] ==True:       
               if Rwallet > 0:
                   pago.motivo=f"orden coffeShop {pago.sede} + recarga de wallet {Rwallet}"
               
               rPago=self.integracionPagos.registrarPago(pago)
               if rPago['status']==True:
                   walletDescuento=self.integracionWallet.descuentowallet(WalletEntity(id=str('x'),idcliente=int(pago.idcliente),monto=float(Dwallet),idpago=str(rPago['response'].id),status=str('aplicado')))
                   walletRecarga=self.integracionWallet.reacargarWallet(WalletEntity(id=str('x'),idcliente=int(pago.idcliente),monto=float(Rwallet),idpago=str(rPago['response'].id),status=str('aplicado')))
                   if walletRecarga['status']==True and walletDescuento['status'] ==True:
                       self.__statusByDeudabyClientebySede__(rPago['response'].id,pago.sede,pago.idcliente)
                       return ResponseInternal.responseInternal(True,"exito al cancelar ls ordenes de los clientes",rPago['response'])               
                   else:
                        return ResponseInternal.responseIternal(False,walletRecarga['mesagge'],walletRecarga['response'])                
               else:
                   return ResponseInternal.responseIternal(False,rPago['mesagge'],rPago['response'])
            else: 
                 return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)      
        finally:
            self.disconnect()
    def __statusByDeudabyClientebySede__(self,idPago:str,sede:str,idCliente:int):
        data=[]
      
        try:
            conection=self.connect()
            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""update ordenes_espacios set idpago='{idPago}',fechapago = now(),status='pagado' where sede= '{sede}' and status = 'por pagar' and idcliente
={idCliente} 
""")
                    self.conn.commit()
                    count=cur.rowcount
                    if count > 0:
                        
                                 
                        return ResponseInternal.responseInternal(True,f"se ecncontraron ({count}) de pedidos  en la sede {sede} del cliente {idCliente} .....!" ,True)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}:No se encontraron deudas del cliente {idCliente} en la sede {sede} ",True)
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
    
    