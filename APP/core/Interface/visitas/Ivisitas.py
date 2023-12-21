from core.Entities.visitas.visitasEntity import VisitasEntity,DetailVisitasEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IVisitas(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def crearVisita(Visita:VisitasEntity)->VisitasEntity:
        pass
    
  
    @abstractmethod
    def salidaVisita(idVisita:str)->bool:
        pass
        
    @abstractmethod
    def getAllVisitasDay(sede:str)->list[VisitasEntity]:
        
        pass
    
    @abstractmethod
    def getFilterByMotivoAndSede(motivo:str,sede:str)-> list[VisitasEntity]:
        pass
    
    @abstractmethod
    def getVisitasByStatus(sede:str,status)->list[VisitasEntity]:
        pass
    @abstractmethod
    def getVisitasDetailToday(sede:str)-> list[DetailVisitasEntity]:
        pass
    