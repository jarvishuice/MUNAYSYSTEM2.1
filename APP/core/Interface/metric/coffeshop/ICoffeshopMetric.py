from core.Entities.metric.coffeshop.CoffeshopMetrictEntity import CoffeshopMetrictEntity
from config.Logs.LogsActivity import Logs
from abc import ABC,abstractmethod
class ImMtericsCoffeshop(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IMectricCoffeshop")
    
    @abstractmethod
    def ExtraerMetricasBysede(sede:str)->CoffeshopMetrictEntity:
        pass
    @abstractmethod
    def ExtraerMetricasGlobal()->CoffeshopMetrictEntity:
        pass
    
    @abstractmethod
    def __extraerAcumuladoVentasMesBySede__(sede:str)->float:
        pass
    @abstractmethod
    def __extraerAcumuladoVentasMesGlobal__()->float:
        pass
    @abstractmethod
    def __extraerAcumuladoVentasDiaBySede__(sede:str)->float:
        pass
    @abstractmethod
    def __extraerAcumuladoVentasDiaGlobal__()->float:
        pass
    @abstractmethod
    def __extraerDeudasBySede__(sede:str)->float:
        pass
    @abstractmethod
    def __extraerDeudasGloabl__()->float:
        pass