from core.Entities.reports.coffeshop.cofeshopReportEntity import DeudaCliente,WalletDisponibles,VentasPorProducto,ReporteCoffeshopEntity,DetallePagos,DetallesPedidos,OrdenesAbiertas,VentasPorClientes,PuntoCount
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class ICierreByFecha(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def __DeudaCleinteBysede__(sede:str)->list[DeudaCliente]:
        pass
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
    def __DetallesPedidos__(sede:str)->list[DetallesPedidos]:
        pass
    @abstractmethod
    def __DetallesPagos__(sede:str)->list[DetallePagos]:
        pass
    @abstractmethod
    def __OrdenesHistoricas__(sede:str)->list[OrdenesAbiertas]:
        pass
    @abstractmethod
    def __ventasPorProducto__(sede:str)-> list[VentasPorProducto]:
        pass
    @abstractmethod
    def __walletDisponible__(sede:str) -> list[WalletDisponibles]:
        pass
    
    
    
    
    @abstractmethod
    def generarCierre(sede:str)->ReporteCoffeshopEntity:
        pass
    