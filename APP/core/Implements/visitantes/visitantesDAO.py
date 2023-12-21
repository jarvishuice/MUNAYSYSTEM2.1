from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Interface.visitas.Ivisitantes import IVisitantes
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.VistantesDataTest.VistantesVAlidacion import VisitantesVAlidacionData
import time
from config.Logs.LogsActivity import Logs

class VisitantesDAO(ConectionsPsqlInterface,IVisitantes):
   
    
    validacion=VisitantesVAlidacionData()
    def __init__(self):
        super().__init__()
    
    
    def crearVisitante(self,cliente: ClientesEntity) -> ClientesEntity:
     try:
       
       cedulaValid=self.validacion.ValidarCi(cliente.ci)
       if type(cedulaValid['response'])!=bool:  
         return ResponseInternal.responseInternal(False,cedulaValid['mesagge'],None)
       else:  
         Nclientes=self.contarVisitante()
         if Nclientes['status'] == False:
            return ResponseInternal.responseInternal(False,Nclientes['mesagge'],None) 
        
         else:   
            conection= self.connect()
            if conection['status']==True:
                with self.conn.cursor() as cur :
                    cliente.id=Nclientes['response']+1
                    cur.execute(f"""insert into visitantes(id,nombre,apellido,correo,tlf,fechaingreso,
                                codigo,credito,ci,identificacion,direccion,deuda)
               values('{cliente.id}','{cliente.nombre}','{cliente.apellido}','{cliente.correo}',
               '{cliente.tlf}',now(),'{cliente.id}',0.00,'{cliente.ci}','{cliente.identificacion}','{cliente.direccion}',0)
                """)
                self.conn.commit()
                return ResponseInternal.responseInternal(True,f"Cliente creado de manera exitoso con el id:[{cliente.id}]",cliente)
            else:
                return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
     except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un cliente con estdo datos {cliente} ",None)
     except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
     except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
     finally:
            self.disconnect()
    def contarVisitante(self) -> int:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute("select id from visitantes order by id desc limit 1")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()
    def buscarVisitante(self,ci: str) -> list[ClientesEntity]:
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                SELECT id, nombre, apellido, correo, tlf, fechaingreso, fechacambio, codigo, credito, ci, identificacion, direccion FROM public.visitantes  WHERE ci ='{ci}' order by id asc
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append( ClientesEntity(id=int(i[0]),nombre=str(i[1]),apellido=str(i[2]),correo=str(i[3]),tlf=str(i[4]),fechaingreso=str(i[5]),ci=str(i[9]),identificacion=str(i[10]),direccion=str(i[11])))
                
                        return ResponseInternal.responseInternal(True,f"Busqueda del cliente [{ci}] realizada con exito s eencotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"BUsqueda sastifactoria per no se encontro ninguna concidencia con algunn cliente cuya cedula sea {ci}",data)    
                 
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
    def getAllVisitantes(self) -> list[ClientesEntity]:
     try: 
        data=[]
        conection= self.connect()
        if conection['status']==True:
                with self.conn.cursor() as cur :
            
                    cur.execute(f"""
                                SELECT id, nombre, apellido, correo, tlf, fechaingreso, fechacambio, codigo, credito, ci, identificacion, direccion FROM public.visitantes   order by id asc
                """)
                    count=cur.rowcount
                    if count > 0:
                       
                                              
                        for i in cur :
                             
                             data.append( ClientesEntity(id=int(i[0]),nombre=str(i[1]),apellido=str(i[2]),correo=str(i[3]),tlf=str(i[4]),fechaingreso=str(i[5]),ci=str(i[9]),identificacion=str(i[10]),direccion=str(i[11])))
                
                        return ResponseInternal.responseInternal(True,f"Extracion de visitantes  realizada con exito se encotraron {count} coincidencas",data)
                    else:
                        return ResponseInternal.responseInternal(True,f"BUsqueda sastifactoria per no se encontro ninguna concidencia con algun visitantes ",data)    
                 
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