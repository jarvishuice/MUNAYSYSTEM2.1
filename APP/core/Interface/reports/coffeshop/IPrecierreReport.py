from core.Entities.reports.coffeshop.cofeshopReportEntity import ReporteCoffeshopEntity,DetallePagos,DeudaCliente,DetallesPedidos,OrdenesAbiertas,VentasPorClientes,PuntoCount
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IPrecierre(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    
    @abstractmethod
    def __OrdenesAbiertas__(sede:str)->list[OrdenesAbiertas]:
        pass
    @abstractmethod
    def __countPunto__(sede:str)->list[PuntoCount]:
        pass
    @abstractmethod
    def __VentasClientes__(sede:str)->list[VentasPorClientes]:
        pass
 
    @abstractmethod
    def __DetallesPagos__(sede:str)->list[DetallePagos]:
        pass
    @abstractmethod
    def generarPrecierre(sede:str)->ReporteCoffeshopEntity:
        pass