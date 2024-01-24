from core.Entities.pagos.pagosEntity import PagosEntity
from core.Entities.tazaDollar.tasaEntity import TasaDollarEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class ItasaDollar(ABC):
    def __init__(self):
        Logs.WirterTask("new implement Ifinance -> TazaDollar")
    @abstractmethod
    def tasaDollarLastRegister()-> float:
        pass
    @abstractmethod
    def updateTasa()-> TasaDollarEntity|bool: ...

    

