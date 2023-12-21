from core.Entities.visitas.visitasEntity import DetailVisitasEntity, VisitasEntity
from core.Interface.visitas.Ivisitas import IVisitas
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.VistantesDataTest.VistantesVAlidacion import VisitantesVAlidacionData
import time
from config.Logs.LogsActivity import Logs
import datetime
class VisitasDao(ConectionsPsqlInterface,IVisitas):
   
    
   
    def __init__(self):
        super().__init__()
    
    def crearVisita(self,Visita: VisitasEntity) -> VisitasEntity:
        try:
            conexion= self.connect()
            Visita.id=time.time()
            if conexion['status']==True:
               with self.conn.cursor() as cur:
                   cur.execute(f"""insert into visitas (id, id_visitante, id_cliente, f_ingreso , status, sede, motivo) 
                               VALUES({Visita.id},{Visita.idVisitante},{Visita.idCliente},now(),'{Visita.status}', '{Visita.sede}','{Visita.motivo}');""")
                   self.conn.commit()
                   return ResponseInternal.responseInternal(True,"Visita registrada de manera satisfactoria",Visita)
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
   
    def salidaVisita(self,idVisita: str) -> bool:
         
     try: 
 
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                update public.visitas set f_salida = now(),status='inactiva' where id = '{idVisita}';
                """)
                    self.conn.commit()
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        
                
                        return ResponseInternal.responseInternal(True,f"Visita #{idVisita} cerrada con exito  "  ,True)
                    else:
                        return ResponseInternal.responseInternal(True,f"{self.NOTE}No se encontraron coincidencias para las visita #({idVisita}) por lo tanto no se pudo cerra ",True)    
                 
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
    def getAllVisitasDay(self,sede:str)->list[VisitasEntity]:
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                select * FROM public.visitas  where Date(f_ingreso) = '{datetime.date.today()}' and sede ='{sede}' order by id  
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append(VisitasEntity(id=str(i[0]),idVisitante=int(i[1]),idCliente=int(i[2]),fIngreso=str(i[3]),fSalida=str(i[4]),status=str(i[5]),sede=str(i[6]),motivo=str(i[7])))
                
                        return ResponseInternal.responseInternal(True,f"Extracion de visitas  realizada con exito se encotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"Extraccion de visitas satisfactoria pero no se han detectado visitas el dia de  hoy ",data)    
                 
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
    def getFilterByMotivoAndSede(self,motivo: str, sede: str) -> list[VisitasEntity]:
    
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                select * FROM public.visitas  where f_ingreso = '{datetime.datetime.today()}' and sede ='{sede}' and motivo= '{motivo}' order by id  asc;
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append(VisitasEntity(id=str(i[0]),idVisitante=int(i[1]),idCliente=int(i[2]),fIngreso=str(i[3]),fSalida=str(i[4]),status=str(i[5]),sede=str(i[6]),motivo=str(i[7])))
                
                        return ResponseInternal.responseInternal(True,f"Extracion de visitas  realizada con exito se encotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"Extraccion de visitas satisfactoria pero no se han detectado visitas el dia de  hoy ",data)    
                 
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
    def getVisitasByStatus(self,sede:str,status)->list[VisitasEntity]:
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                select * FROM public.visitas  where  sede ='{sede}' and status= '{status}' order by id  asc;
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append(VisitasEntity(id=str(i[0]),idVisitante=int(i[1]),idCliente=int(i[2]),fIngreso=str(i[3]),fSalida=str(i[4]),status=str(i[5]),sede=str(i[6]),motivo=str(i[7])))
                
                        return ResponseInternal.responseInternal(True,f"Extracion de visitas  realizada con exito se encotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"Extraccion de visitas satisfactoria pero no se han detectado visitas el dia de  hoy ",data)    
                 
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
    def getVisitasDetailToday(self,sede: str) -> list[DetailVisitasEntity]:
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                               select v.id,v2.nombre as visitor,v2.correo,v2.ci,c.nombre as cliente, to_char(v.f_ingreso,'hh12:MI:SS AM') as horaingreso ,to_char(v.f_salida,'hh12:MI:SS AM') as hora_salida ,v.status ,v.sede ,v.motivo from visitas v 
inner join visitantes v2 on v2.nombre = v2.nombre and v2.correo=v2.correo and v2.ci=v2.ci
inner join clientes c on c.nombre = c.nombre
where c.id = v.id_cliente and v2.id =v.id_visitante and sede= '{sede}'  and DATE(v.f_ingreso) = '{datetime.date.today()}'
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append(DetailVisitasEntity(id=str(i[0]),visitante=str(i[1]),correo=str(i[2]),ci=str(i[3]),cliente=str(i[4]),fIngreso=str(i[5]),fSalida=str(i[6]),status=str(i[7]),sede=str(i[8]),motivo=str(i[9])))
                
                        return ResponseInternal.responseInternal(True,f"Extracion de visitas  realizada con exito se encotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"Extraccion de visitas satisfactoria pero no se han detectado visitas el dia de  hoy ",data)    
                 
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
         
        
         