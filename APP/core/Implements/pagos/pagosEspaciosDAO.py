from core.Entities.pagos.pagosEntity import PagosEntity,PagosDetailEntity
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Interface.pagos.Ipagos import IPagos
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.clienteDataTest.clienteVAlidacion import CLientesVAlidacionData
from core.Implements.wallet.walletEspaciosDAO import WalletEspaciosDAO,WalletEntity
import time
from config.Logs.LogsActivity import Logs
class PagosEspaciosDAO(ConectionsPsqlInterface,IPagos):
    wallet=WalletEspaciosDAO()
    def __init__(self):
        super().__init__()
    def registrarPago(self,pagoData: PagosEntity) -> PagosEntity:
        try:
            tazaSql="select id from tazadollar t  order by id desc limit 1 " #obtemner el id de la ultima taza registrada
            
            conexion = self.connect()
            pagoData.id = time.time()#el id del pago es generado con la fecha fdormato unix 
            if conexion['status'] ==True:
                with self.conn.cursor() as cur :
                    cur.execute(f""" insert into pagos_espacios (id,idcliente,fechapago,motivo,idformadepago,referencia,monto,idtaza,sede) values(
                        '{pagoData.id}',{pagoData.idcliente},now(),'{pagoData.motivo}',{pagoData.idformadepago},'{pagoData.referencia}',
                        '{pagoData.monto}',({tazaSql}),'{pagoData.sede}')""")
                    self.conn.commit()
                return ResponseInternal.responseInternal(True,f"pago regiustrado de manera satisfactoira {pagoData.id}",pagoData)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un PAGO con estdo datos {pagoData} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
            Logs.WirterTask(f"finalizado el registro del pago {pagoData.id}")
    
    def registrarAbono(self,pagoData: PagosEntity) -> PagosEntity:
        try:
            pagoData.motivo="Abono deuda Espacios"
            pago=self.registrarPago(pagoData)
            if pago['status']==True:
                wallet=self.wallet.reacargarWallet(WalletEntity(id=str(time.time()),idcliente=int(pagoData.idcliente),monto=float(pagoData.monto),idpago=str(pago['response'].id),status=str('aplicado')))
                if wallet['status'] ==True:
                    return ResponseInternal.responseInternal(True,"Abono registrado de anera correcta",pago['response'])
                else:
                    return ResponseInternal.responseInternal(False, wallet['mesagge'],None)
            else:
                return ResponseInternal.responseInternal(False,pago['mesagge'],None) 
        finally:
            self.disconnect()
            Logs.WirterTask(" ha finalizado la ejecuscion del registro de abonos")
    def registroMultipago(self,pagoData:PagosEntity)->PagosEntity:
        try:
            pagoData.motivo=f"Multipago coffeshop {pagoData.sede}"
            pago=self.registrarPago(pagoData)
            if pago['status']==True:
                wallet=self.wallet.reacargarWallet(WalletEntity(id=str(time.time()),idcliente=int(pagoData.idcliente),monto=float(pagoData.monto),idpago=str(pago['response'].id),status=str('aplicado')))
                if wallet['status'] ==True:
                    return ResponseInternal.responseInternal(True,"Abono registrado de anera correcta",pago['response'])
                else:
                    return ResponseInternal.responseInternal(False, wallet['mesagge'],None)
            else:
                return ResponseInternal.responseInternal(False,pago['mesagge'],None) 
        finally:
            self.disconnect()
            Logs.WirterTask(" ha finalizado la ejecuscion del registro de abonos")
    def editPay(self,pagoData:PagosEntity)-> bool:
        try:
           
            conection = self.connect()
            if conection['status'] == True:
                with self.conn.cursor() as cur :
                    cur.execute(f"""
                                update pagos_espacios set idformadepago = {pagoData.formadepago} , fechapago = {pagoData.fecha}
                                where id = '{pagoData.id}';
                                """)
                    self.conn.commit()             
                    count=cur.rowcount
                    if count > 0:
                        return ResponseInternal.responseInternal(True,f"exito al actualizar el pago #[{pagoData.id}]",True)
                    else:
                        return ResponseInternal.responseInternal(True,f"no se pudo actualizar el cliente  puede que no exista ningun cliente con dicho id  ",True)    
                    
            else:
                 return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"puede que no exista ningun cliente con dicho id  ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
        
            self.disconnect()       
            Logs.WirterTask(" ha finalizado la ejecucion de la ediccion de pagos ")
            
    def getAllPayDetail(self,sede: str) -> PagosDetailEntity: 
        try:
          data=[]
          conection= self.connect()
          if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                               select p.id,p.fechapago,p.monto,p.motivo,c.nombre as cliente,f.metodo as formadepago,p.referencia,t.precio as tasa, 
p.sede,p.idcliente,p.idformadepago from pagos_espacios p
inner join clientes c on c.nombre = c.nombre 
inner join fromadepago f on f.metodo = f.metodo 
inner join tazadollar t on t.precio = t.precio
where p.sede = '{sede}' and c.id = p.idcliente and f.id = p.idformadepago  and t.id = p.idtaza order by p.fechapago desc limit 100;
                """)
                    count=cur.rowcount
                    if count > 0:
                        for i in cur :
                             data.append(PagosDetailEntity(id=str(i[0]),fecha=str(i[1]),monto=float(i[2]),motivo=str(i[3]),cliente=str(i[4]),formaDepago=str(i[5]),referencia=str(i[6]),tasa=float(i[7]),sede=str(i[8]),idcliente=int(i[9]),idformadepago=int(i[10])))
                
                        return ResponseInternal.responseInternal(True,f"leyendo todos  los pagos  de la sede {sede} se encontraron {count} pagos registrados  !!",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"error a leer la tabla pagos puede que la lista este vacia ",data)    
                 
          else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()