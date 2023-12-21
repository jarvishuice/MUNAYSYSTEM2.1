from core.Interface.auth.Iauth import IAuth
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Interface.clients.IClientes import IClientes
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface

import time
from config.Logs.LogsActivity import Logs
class AuthDAO(ConectionsPsqlInterface,IAuth):

    def __init__(self):
        super().__init__()
        
    def validarToken(self, token) -> bool:
        try:
             
            conexion=self.connect()
            
            if conexion['status'] == True:
                    with self.conn.cursor() as cur :
                        cur.execute(f"""select *  from usuarios where token = '{token}' and status='conectado' """)
                        count= cur.rowcount
                        if count > 0:
                                                
                            return ResponseInternal.responseInternal(True,f"token validado con exito!!!",True)                                       
                        else : 
                            return ResponseInternal.responseInternal(False,f"{self.ERROR } ALERTA ESTAN INGRESANDO UN TOKEN ERRONEO POSIBLE  CYBER ATAQUE",False)
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