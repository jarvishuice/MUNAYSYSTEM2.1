import time
from core.Entities.wallet.walletEntity import WalletEntity
from core.Interface.wallet.Iwallet import IWallet
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from config.Logs.LogsActivity import Logs
from core.test.walletDataTest.walletValidationDataTest import ValidacionWalletData
class WalletDAO(ConectionsPsqlInterface,IWallet):
    validacion=ValidacionWalletData()
    def __init__(self):
        super().__init__()
    validacion= ValidacionWalletData()
    def consultaSaldo(self,idCliente: int) -> float:
        try:
            saldo = 0
            conexion= self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur :
                    cur.execute(f""" select COALESCE(NULLIF(sum(monto), NULL),0 ) as saldo from wallet where idcliente={idCliente}""")
                    count=cur. rowcount
                    if count > 0:
                        for i in cur:
                            saldo=i[0]
                        return ResponseInternal.responseInternal(True, f"Consulta de saldo exitosa del cliente ({idCliente}) su saldo es {saldo}",saldo)
                    else:
                        return ResponseInternal.responseInternal(True, f"Consulta de saldo exitosa del cliente ({idCliente}) pero no se encontraron registros",saldo)
                        
                    
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
            
            
    def descuentowallet(self,wallet: WalletEntity) -> WalletEntity:
        try:
            wallet.id=time.time()
            conexion= self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur :
                                                                                                                                                                                                                     
                    cur.execute(f""" insert into wallet (idcliente,id,idpago,status,monto) values({wallet.idcliente},{wallet.id},{wallet.idpago},'{wallet.status}',
                            
                                {self.validacion.validarMonto(wallet.monto) })""") # el metodo validarMonto se encarga de ver si el monto es mayor a cero pasarlo a negativo y en caso contrario preserva el monto 
                    self.conn.commit()
             
                        
                    return ResponseInternal.responseInternal(True, f"descuento de wallet realizado de manera correcta ({wallet}) ",wallet)
                        
                    
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
    def reacargarWallet(self,wallet: WalletEntity) -> WalletEntity:
        try:
            wallet.id=time.time()
            conexion= self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur :
                                                                                                                                                                                                                     
                    cur.execute(f""" insert into wallet (idcliente,id,idpago,status,monto) values({wallet.idcliente},{wallet.id},{wallet.idpago},'{wallet.status}',
                            
                                {wallet.monto})""") 
                    self.conn.commit()
             
                        
                    return ResponseInternal.responseInternal(True, f"recarga  de wallet realizado de manera correcta ({wallet}) ",wallet)
                        
                    
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
    
                
        