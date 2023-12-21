from core.Entities.pagos.pagosEntity import PagosEntity
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Interface.pagos.Ipagos import IPagos
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.clienteDataTest.clienteVAlidacion import CLientesVAlidacionData
from core.Implements.wallet.walletDAO import WalletDAO,WalletEntity
import time
from config.Logs.LogsActivity import Logs
class PagosDAO(ConectionsPsqlInterface,IPagos):
    wallet=WalletDAO()
    def __init__(self):
        super().__init__()
    def registrarPago(self,pagoData: PagosEntity) -> PagosEntity:
        try:
            tazaSql="select id from tazadollar t  order by id desc limit 1 " #obtemner el id de la ultima taza registrada
            
            conexion = self.connect()
            pagoData.id = time.time()#el id del pago es generado con la fecha fdormato unix 
            if conexion['status'] ==True:
                with self.conn.cursor() as cur :
                    cur.execute(f""" insert into pagos (id,idcliente,fechapago,motivo,idformadepago,referencia,monto,idtaza,sede) values(
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
            pagoData.motivo="Abono deuda coffeshop"
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