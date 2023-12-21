from core.Entities.pedidos.pedidosEntity import PedidosEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IPedidos(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IOrdenes")
    
    @abstractmethod
    def crearPedido(orden:PedidosEntity,sede)->PedidosEntity:
        pass
    @abstractmethod
    def regVariosPedido(self,pedidos:list[PedidosEntity])->list[PedidosEntity]:
        pass
            
    """@abstractmethod
    def actualizarPagoOrden(idPago:str,idOrden)->OrdenesEntity:
        pass"""
    """@abstractmethod
    def leerTodosLosPedidos(sede:str)-> list[PedidosEntity|None]:
        pass
    @abstractmethod
    def OrdenesFilterByStatusAndSede(status,sede)->list[PedidosEntity|None]:
        pass"""
        