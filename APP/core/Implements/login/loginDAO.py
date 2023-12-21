from core.Entities.user.loginEntity import LoginEntity
from core.Entities.user.usersEntity import UsersEntity
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Interface.Login.Ilogin import ILogin
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.clienteDataTest.clienteVAlidacion import CLientesVAlidacionData
from core.Implements.user.userDAO import UserDAO
from werkzeug.security import generate_password_hash,check_password_hash
import time
from config.Logs.LogsActivity import Logs

class LogginDAO(ILogin):
    user=UserDAO()
    
    def __init__(self):
        super().__init__()
        
    def IniciarSeccion(self,login:LoginEntity) -> LoginEntity:
        try:
            usuarioValidador= self.user.busquedaUsuario(login.nombreUsuario)
            if usuarioValidador['status']== True:
                print(type(usuarioValidador['response']))
                self.__validacionLogin__(login,usuarioValidador['response'])
                self.user.cambiarEstatus(usuarioValidador['response'],"conectado")
                usuarioValidador['response'].token=self.__generarToken__() 
                self.user.actualizarToken(usuarioValidador['response'])
                usuarioValidador['response'].password= str('🖕')
                return ResponseInternal.responseInternal(True,f" El usuario {login.nombreUsuario} ha iniciado seccion correctamente",usuarioValidador['response'])
            else:
                return ResponseInternal.responseInternal(False,usuarioValidador['mesagge'],usuarioValidador['response'])
        finally:
            Logs.WirterTask("culminado la ejecucion de inicio de seccion LoginDAO") 
        
    def __validarPasword__(passWord:str,passWordGood:str) -> bool:
             if check_password_hash(passWord,passWordGood):
                 return True
             else : return False
         
    def __validarUser__(userName:str,userNameGood:str) -> bool:
        if userName == userNameGood:
            return True
        else:
            return False
    def __generarToken__(self) -> str:
        return "holamuunod"
    
    def __validacionLogin__(self,Login: LoginEntity,user:UsersEntity) -> UsersEntity:
     
        
         userVAlidacion=self.__ValidarUsuario__(userName=Login.nombreUsuario,userNameGood=user.nombreusuario)
         validacionPassword=self.__ValidarPass__(passWord=Login.nombreUsuario,passwordGood=user.password)
         if userVAlidacion==True and validacionPassword ==True and user.status == 'activo':
             return  ResponseInternal.responseInternal(True,f"el usuario {Login.nombreUsuario } ha iniciado seccion de manera correcta ",user)
         else: return ResponseInternal.responseInternal(False,f"usuario o contrasena errada por favor validelos",None)
    def __ValidarUsuario__(self, userName: str, userNameGood: str) -> bool:
       if userName == userNameGood:
            return True
       else:
            return False
    def __ValidarPass__(self, passWord: str, passwordGood: str) -> bool:
        if check_password_hash(passWord,passwordGood):
                 return True
        else : 
            return False
    def cerrarSeccion(self, user: UsersEntity) -> bool:
         try:
            trigger=self.user.cambiarEstatus(user,"activo")
            if trigger['status']== True:
                return ResponseInternal.responseInternal(True,f"seccion del usuario{str(user)} cerrada con exito",True)
            else: 
                return ResponseInternal.responseInternal(False,trigger['mesagge'],False)
         finally:
             Logs.WirterTask("finalizada la ejecuciondel del core cerrar seccion !!!!!")
    