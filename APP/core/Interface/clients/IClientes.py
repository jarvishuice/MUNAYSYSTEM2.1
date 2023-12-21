from core.Entities.clientes.clientesEntity import ClientesEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IClientes(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def crearCliente(cliente:ClientesEntity)->ClientesEntity:
        pass
    
    @abstractmethod
    def contarClientes()->int:
        pass
    @abstractmethod
    def buscarClientes(nombre:str)->list[ClientesEntity]:
        pass
    @abstractmethod
    def getAllClientes()->list[ClientesEntity]:
        pass
    @abstractmethod
    def editCliente(cliente:ClientesEntity)->ClientesEntity:
        pass        