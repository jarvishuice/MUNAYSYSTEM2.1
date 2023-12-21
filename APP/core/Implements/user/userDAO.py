from core.Entities.user.usersEntity import UsersEntity
from core.Interface.User.Iuser import IUser
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from werkzeug.security import generate_password_hash,check_password_hash
import time
from config.Logs.LogsActivity import Logs
class UserDAO(ConectionsPsqlInterface,IUser):

    def __init__(self):
        super().__init__()
    
    def crearUser(self,usuario:UsersEntity) -> UsersEntity:
    
        try:
         idUsuario=self.___ContarUsuarios__()
         if idUsuario['status']== True:
                    
            conexion=self.connect()
            usuario.password=generate_password_hash(usuario.password,"pbkdf2:sha256:30",12)
            if conexion['status'] == True:
                    with self.conn.cursor() as cur :
                        cur.execute(f"""insert into usuarios(id,nombre,apellido,ci,nombreusuario,password,token,tipouser,urlimg,status) values({idUsuario['response']},'{usuario.nombre}'
                                    ,'{usuario.apellido}','{usuario.ci}','{usuario.nombreusuario}','{usuario.password}',
                                    '{usuario.password}','{usuario.tipoUsuario}','{usuario.urlImagen}','activo')""")
                        self.conn.commit()
                        return ResponseInternal.responseInternal(True,f"usuario registrado con exito detail[{dict(usuario)}]",usuario)                                       
            else:   
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
         else:
             return ResponseInternal.responseInternal(False,"ERROR al validar el ususario...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un usuario con las mismas caracteristicas {usuario} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    def ___ContarUsuarios__(self):
        try:
            respuesta = None
            conexion=self.connect()
            
            if conexion['status'] == True:
                    with self.conn.cursor() as cur :
                        cur.execute(f"""select id as cantidad  from usuarios  order by id desc limit 1; """)
                        for i in cur:
                            respuesta= i[0] +1
                        return ResponseInternal.responseInternal(True,f"usuario contado con exito con exito !!!",respuesta)                                       
            else:   
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un usuario con las mismas caracteristicas  ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    def busquedaUsuario(self,userName: str) -> UsersEntity:
        try:
           
            conexion=self.connect()
            
            if conexion['status'] == True:
                    with self.conn.cursor() as cur :
                        cur.execute(f"""select *  from usuarios where nombreusuario = '{userName}' """)
                        count= cur.rowcount
                        if count > 0:
                            for i in cur:
                                respuesta=UsersEntity(id=int(i[0]),nombre=str(i[1]),apellido=str(i[2]),ci=str(i[3]),nombreusuario=str(i[4]),password=str(i[5]),token=str(i[6]),tipoUsuario=int(i[7]) or 0 ,urlImagen=str(i[8]),status=str(i[9]))
                            return ResponseInternal.responseInternal(True,f"usuario contado con exito con exito !!!",respuesta)                                       
                        else : 
                            return ResponseInternal.responseInternal(False,"NO se ha encontrado ningun  usuario ({username})",None)
            else:       
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un usuario con las mismas caracteristicas {usuario} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
            
            
            
    def cambiarEstatus(self,credential: UsersEntity, newStatus: str) -> UsersEntity:
        try:
            credential.status=newStatus
            conexion= self.connect()
            if conexion['status'] ==True:
              with self.conn.cursor() as cur :
                  cur.execute(f"update usuarios set status='{newStatus}' where id={credential.id}")
                  self.conn.commit()
                  count = cur.rowcount
                  if count > 0:
                      return ResponseInternal.responseInternal(True,"estatus de usuario cambiando con exito ",credential)
                                         
            else:   
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un usuario con las mismas caracteristicas {usuario} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    def actualizarToken(self,credential: UsersEntity) -> UsersEntity:
        try:
            credential.token= str(time.time())
            conexion= self.connect()
            if conexion['status'] ==True:
              with self.conn.cursor() as cur :
                  cur.execute(f"update usuarios set token='{credential.token}' where id={credential.id}")
                  self.conn.commit()
                  count = cur.rowcount
                  if count > 0:
                      return ResponseInternal.responseInternal(True,f"token del usuario {credential.nombreusuario} con exito ",credential)
                                         
            else:   
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error debido a que ya existe un usuario con las mismas caracteristicas {credential} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
        
            
        
        
    
            
    
    
     