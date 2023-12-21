from core.Entities.clientes.clientesEntity import ClientesEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IVisitantes(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def crearVisitante(cliente:ClientesEntity)->ClientesEntity:
        pass
    
    @abstractmethod
    def contarVisitante()->int:
        pass
    @abstractmethod
    def buscarVisitante(ci:str)->list[ClientesEntity]:
        pass
        
    @abstractmethod
    def getAllVisitantes()->list[ClientesEntity]:
        pass