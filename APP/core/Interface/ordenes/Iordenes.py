from core.Entities.ordenes.ordenesEntity import OrdenesEntity,OrdenesDetalladasEntity
from core.Entities.ordenes.detalleOrdenEntity import OrdenDetalladaEntity,DetalleOrdenesEntity

from core.Entities.clientes.deudaClienteCoffeShopEntitity import DetalleDedudaClientesEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IOrdenes(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IOrdenes")
    
    @abstractmethod
    def crearOrden(orden:OrdenesEntity)->OrdenesEntity:
        pass
    """@abstractmethod
    def actualizarPagoOrden(idPago:str,idOrden)->OrdenesEntity:
        pass"""
    @abstractmethod
    def OrdenesPorPagarBysede(sede:str)-> list[OrdenesEntity|None]:
        pass
    @abstractmethod
    def OrdenesFilterByStatusAndSede(status,sede)->list[OrdenDetalladaEntity|None]:
        pass
    @abstractmethod
    def OrdenesAbiertasByClienteAndSede(idCliente:int,sede:str)-> list[OrdenesEntity]: 
        pass
    @abstractmethod
    def OrdenesDeLajornada(sede:str)->list[OrdenesEntity]:
        pass
    @abstractmethod 
    def getDetailOrden(idOrden:str)->list[OrdenDetalladaEntity]:
        pass
    """_summary_
    #{metodo que returna todos las pordenes de una sedes}
    """
    @abstractmethod 
    def getOrdenesBysede(sede:str)->list[OrdenesDetalladasEntity|None]:
        pass
    @abstractmethod 
    def deleteOrder(idOrder:str)->bool:
        pass