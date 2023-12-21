



from core.Interface.finance.ItazaDollar import ItasaDollar
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface

from config.Logs.LogsActivity import Logs
""" Esta clase es la encargada de gestiionar todo lo  referentes a llas operaciones que se realizararn con el wallet contemplando la tabla de pagos 
esta complementa a wallet DAo 
el atrubuto wallet es la implementacion de walletDAO donde esta toda la lohgiaca para insertar en  la tabla wallet 

    """
class TasaDollarDAO(ConectionsPsqlInterface,ItasaDollar):

    def __init__(self):
        super().__init__()
    
    def tasaDollarLastRegister(self) -> float:
        try:
            respuesta=0
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                             select precio from tazadollar t  order by id desc limit 1    
                """)
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 : 
                        for i in cur :
                         respuesta=float(i[0])
                        return  ResponseInternal.responseInternal(True,f"consulta de ultima tasa Dollar BCV  realizada con exito ",respuesta)
                    else:
                        
                        return ResponseInternal.responseInternal(False, f"{self.NOTE} no se encontraron registros del dollar  () ",None)
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
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
             

        