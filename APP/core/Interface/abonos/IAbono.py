from core.Entities.abonos.abonoEntity import AbonosEntity
from abc import ABC,abstractmethod

class IAbonos(ABC):
    @abstractmethod
    def registrarAbono(self,abono:AbonosEntity): ...
    
    @abstractmethod
    def getAbono(self,idCliente:int,sede:str): ...
    



