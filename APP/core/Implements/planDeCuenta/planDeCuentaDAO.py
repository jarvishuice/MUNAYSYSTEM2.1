
from core.Entities.PlanDeCuentas.PlanDeCuentas import PlanDeCuentaEntity
from core.Interface.PlandeCuenta.IplanDeCuenta import IPlanDeCuenta
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface

import time
from config.Logs.LogsActivity import Logs
class PlanDeCuentaDAO(ConectionsPsqlInterface,IPlanDeCuenta):

    def __init__(self):
        super().__init__()
    def getFormPayBySede(self,sede)->list[PlanDeCuentaEntity]:
        try:
            data=[]
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                                select * from fromadepago f where sede = '{sede.upper()}' or sede ='AMBAS'
                """)
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 : 
                        for i in cur :
                          data.append(PlanDeCuentaEntity(id=int(i[0]),banco=str(i[1]),nCuenta=str(i[2]),metodo=str(i[3]),sede=str(i[4])))
                        return  ResponseInternal.responseInternal(True,f"Busqueda de plan de cuentas en la sede {sede} se encontraron ({count}) coincidencias",data)
                    else:
                        
                        return ResponseInternal.responseInternal(True, f"{self.NOTE} no se encontraron coincidencas para los plannes de cuenta de la sede {sede} ",None)
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
    