
from config.Logs.LogsActivity import Logs
from core.Entities.clientes.clientesEntity import ClientesEntity
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.config.ResponseInternal import ResponseInternal

class CLientesVAlidacionData(ConectionsPsqlInterface):
    def __init__(self) -> None:
        pass
    def ValidarCi(self,ci):
        try:
           
            conexion= self.connect()
            if conexion['status'] == True:
                with self.conn.cursor() as cur :
                    cur.execute(f"select id,nombre,fechaingreso,correo from clientes where ci='{ci}' ")
                    count=cur.rowcount
                    if count > 0:
                        
                           
                            
                            
                        return ResponseInternal.responseInternal(False,"ya exiten estea cedula pertenece a un un  usuario ",None)
                    else:
                        return ResponseInternal.responseInternal(True,"validacionde cedula culminada coexito",True)
            else:
                return ResponseInternal.responseInternal(False, "erro de conexion al abase de datos",None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"error en la base de datos detail[{e}]") 
        finally:
            self.disconnect()