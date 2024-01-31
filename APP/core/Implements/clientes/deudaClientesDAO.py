from core.Entities.pagos.pagosEntity import PagosEntity
from core.Entities.clientes.deudaClienteCoffeShopEntitity import DetalleDedudaClientesEntity, DeudaClienteCoffeShopEntity 
from core.Interface.clients.IdeudaClientes import IDedudaClientes
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.clienteDataTest.clienteVAlidacion import CLientesVAlidacionData
from core.Implements.pagos.pagosDAO import PagosDAO
from core.Implements.pagos.pagosWalletDAO import PagosWalletDAO
from core.Implements.wallet.walletDAO import WalletDAO,WalletEntity
from core.Implements.Abonos.abonoDAO import AbonoDAO,AbonosEntity
import time
from config.Logs.LogsActivity import Logs
class DeudaCientesDAO(ConectionsPsqlInterface,IDedudaClientes):
    """_summary_

    Args:
        ConectionsPsqlInterface (_type_): Conector a la base de datos
        IDedudaClientes (_type_): Interface  de deudas clientes
    """    """
    """
    def __init__(self):
        super().__init__()
    #modulo de pagos
    integracionPagos=PagosDAO()

    
    #modulo de wallet
    integracionWalletPagos=PagosWalletDAO()
   
    #modulo de wallet
    integracionWallet=WalletDAO()
    #modulo de integraciones
    integracionAbono= AbonoDAO()
    def getDeudasClientesBySede(self,sede) -> list[DeudaClienteCoffeShopEntity]:
        """ obtener la deuda de los clientes
        Args:
            sede (_type_): _description_

        Returns:
            list[DeudaClienteCoffeShopEntity]: _description_
             """
        
        try:
            conection= self.connect()  
            data=[]

            if conection['status']==True:
                with self.conn.cursor() as cur :
                    #cur.execute(f"""select sum (o.total) as deuda,count(o.total) as cantidad_ordenes,c.nombre,c.id,c.ci from  ordenes o
#inner join clientes c on c.nombre=c.nombre and c.id=c.id and c.ci =c.ci
#where o.status ='por pagar' and o.sede='{sede}' and c.id=o.idcliente  
#group by c.nombre ,c.id""")
                    cur.execute(f""" SELECT SUM(o.total) AS deuda, COUNT(o.total) AS cantidad_ordenes,
                                    c.nombre,
                                    c.id,
                                    c.ci,
                                    (SELECT COALESCE(SUM(a.monto), 0) FROM abonos a WHERE a.idcliente = c.id AND a.sede = '{sede}') AS saldo
                                    FROM 
                                    ordenes o
                                    INNER JOIN 
                                    clientes c ON c.id = o.idcliente
                                    WHERE 
                                    o.status = 'por pagar' AND o.sede = '{sede}'
   
                                    GROUP BY 
                                    c.nombre, c.id, c.ci
                                    order by c.nombre asc;""")
                    count=cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(DeudaClienteCoffeShopEntity(idCliente=int(i[3]),ci=str(i[4]),nombre=str(i[2]),cantidadOrdenes=int(i[1]),deuda=float(i[0]),abono=float(i[5])))     
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
                    cur.execute(f"""select o.fechaPedido,i.nombre,p.cantidad,p.total,p.idorden  from pedidos p
inner join productos i on i.nombre=i.nombre
inner join ordenes o on o.fechapedido = o.fechapedido
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
        """_summary_

        Args:
            pago (PagosEntity): Entdad de pago
            Rwallet (float): monto a recaragar en wallet
            Dwallet (float): monto a decortar en abono

        Returns:
            PagosEntity: entifidade de registro de pago
        """        """
        """
        if Dwallet > 0:
            Dwallet = Dwallet * -1
        try:
            conexion= self.connect()
            if conexion['status'] ==True:       
               if Rwallet > 0:
                   pago.motivo=f"orden coffeShop {pago.sede} + recarga de wallet {Rwallet}"
               
               rPago=self.integracionPagos.registrarPago(pago)
               if rPago['status']==True:
                   abonoDescuento=self.integracionAbono.registrarAbono(AbonosEntity(id=str('x'),idCliente=int(pago.idcliente),idPago=str(rPago['response'].id),status= str("aplicado").upper(),monto=float(Dwallet),sede=str(rPago['response'].sede)))
                   walletRecarga=self.integracionWallet.reacargarWallet(WalletEntity(id=str('x'),idcliente=int(pago.idcliente),monto=float(Rwallet),idpago=str(rPago['response'].id),status=str('aplicado')))
                   if walletRecarga['status']==True and abonoDescuento['status'] ==True:
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
                    cur.execute(f"""update ordenes set idpago='{idPago}',fechapago = now(),status='pagado' where sede= '{sede}' and status = 'por pagar' and idcliente
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
    
    