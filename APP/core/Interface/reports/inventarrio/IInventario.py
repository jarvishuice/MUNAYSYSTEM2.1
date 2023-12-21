from core.Entities.reports.inventario.ItemsInventarioEntity import ItemsInventarioEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IInventario(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def __extraerInventario__(sede:str)->ItemsInventarioEntity:
        pass
    @abstractmethod
    def generarReporte(sede:str):
        pass