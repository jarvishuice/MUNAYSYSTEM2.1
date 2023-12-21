from core.Entities.user.usersEntity import UsersEntity
from core.Entities.user.loginEntity import LoginEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class ILogin(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IOrdenes")
    
    @abstractmethod
    def IniciarSeccion(login:LoginEntity)->LoginEntity:
        pass
   
    @abstractmethod
    def __validarPasword__(self,passWord:str,passwordGood:str)->bool:
        pass
    @abstractmethod
    def __validacionLogin__(self,Login:LoginEntity,user:UsersEntity)->UsersEntity:
        pass
    @abstractmethod
    def __generarToken__()->str:
        
        pass
    @abstractmethod
    def __validarUser__(self,userName:str,userNameGood:str)->bool:
        pass
    @abstractmethod 
    def __ValidarUsuario__(self,userName:str,userNameGood:str)->bool:
        pass
    @abstractmethod
    def __ValidarPass__(self,passWord:str,passwordGood:str)->bool:
        pass
    
    @abstractmethod
    def cerrarSeccion(self,user:UsersEntity)->bool :
        pass
    
 