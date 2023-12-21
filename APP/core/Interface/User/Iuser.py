from core.Entities.user.usersEntity import UsersEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
""" ##########################
interface para la gestion de los usuarios 
    ###############################"""
class IUser(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IOrdenes")
    
    @abstractmethod
    def crearUser(credential:UsersEntity)->UsersEntity:
        pass 
    @abstractmethod
    def ___ContarUsuarios__(self):
        pass
    @abstractmethod
    def busquedaUsuario(credential:UsersEntity)->UsersEntity:
        pass
    @abstractmethod
    def cambiarEstatus(credential:UsersEntity,newStatus:str)->UsersEntity:
        pass
    @abstractmethod
    def actualizarToken(credential:UsersEntity)->UsersEntity :
        pass
""" @abstractmethod
    def cambiarContrasena(credential:UsersEntity,passwordNew:str)->UsersEntity:
        pass
    @abstractmethod
    def verUsuarios()->UsersEntity:
        pass
    @abstractmethod
    def filtarUsuariosPortipo(tipo:int)->list[UsersEntity]:
        pass
    @abstractmethod
    def filtrarUsuariosPorStatus(status:str)->list[UsersEntity]:
        pass 
"""

  
        