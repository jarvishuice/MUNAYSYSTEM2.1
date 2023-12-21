from core.Entities.pedidos.pedidosEntity import PedidosEntity
from abc import ABC,abstractmethod
class IAuth(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def validarToken(self,token)->bool:
        pass