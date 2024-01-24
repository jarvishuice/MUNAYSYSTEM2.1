
import time
from core.Interface.finance.ItazaDollar import ItasaDollar,TasaDollarEntity
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from providers.Services.finance import Finance
from config.Logs.LogsActivity import Logs

class TasaDollarDAO(ConectionsPsqlInterface,ItasaDollar):
    """
    Esta es la clase 'TasaDollarDAO'.

    Argumentos:
    ConectionsPsqlInterface (type): La interfaz de conexión para la base de datos PostgreSQL.
    ItasaDollar (type): La interfaz para ItasaDollar.

    Retorna:
    type: El tipo de la clase.
"""
    
    def __init__(self):
        self.finance = Finance()
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
             
    def updateTasa(self)->TasaDollarEntity|bool: 
        """_summary_

        Returns:
            :TasaDollarEntity|bool: _description_
        """        
        try:
            precio = self.finance.getTasaBcv()
            if precio == False:
                return ResponseInternal.responseInternal(False,f"No se pudo obtener la tasa del dia ",False)
            tasa=TasaDollarEntity(id=str(time.time()),precio=float(precio))
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                              INSERT INTO public.tazadollar (id, precio) VALUES('{tasa.id}', {tasa.precio});    
                """)
                    self.conn.commit()
                
                    return  ResponseInternal.responseInternal(True,f"consulta de ultima tasa Dollar BCV  realizada con exito ",tasa)
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
               