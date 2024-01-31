import datetime
import time
from core.Entities.abonos.abonoEntity import AbonosEntity

from core.Interface.abonos.IAbono import IAbonos
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.ordenesDataTest.ordenesValidation import validationOrdenesData

from core.Implements.pedidos.pedidosDAO import PedidosDAO
from core.Implements.wallet.walletDAO import WalletDAO

from config.Logs.LogsActivity import Logs

class AbonoDAO(IAbonos,ConectionsPsqlInterface):
    def __init__(self):
        super().__init__()
        
    
    def registrarAbono(self,abono:AbonosEntity):
        try:
            abono.id= time.time()
            conection= self.connect()
            if conection['status'] == False:
                Logs.WirterTask(f"{self.ERROR} error de conexion lal servidor de BD")
                return ResponseInternal.ResponseInternal(False,"error de conexion a la base de datos",None)
            with self.conn.cursor() as cur:
                cur.execute(f"insert into abonos (id,idcliente,idpago,status,monto,sede)  values('{abono.id}',{abono.idCliente},'{abono.idPago}','{abono.status}',{abono.monto},'{abono.sede}')")
                self.conn.commit()
                return ResponseInternal.responseInternal(True,f"Abono registrado con exito!!! detail [{abono}]",abono)
            
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un abono rgistrado con esos datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()     
    def getAbono(self,idCliente:int,sede:str): 
        try:
            data = []
            
            conection= self.connect()
            if conection['status'] == False:
                Logs.WirterTask(f"{self.ERROR} error de conexion lal servidor de BD")
                return ResponseInternal.ResponseInternal(False,"error de conexion a la base de datos",None)
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT COALESCE(SUM(monto), 0)  from abonos a  where idcliente = {idCliente} and sede = '{sede}'")
                for i in cur:
                    data.append(i[0])
                return ResponseInternal.responseInternal(True,f"Abono registrado con exito!!! detail ",data[0])
            
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un abono rgistrado con esos datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect() 
        
        
            
