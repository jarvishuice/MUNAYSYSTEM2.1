from core.Entities.pagos.pagosEntity import PagosEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IPagos(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IPagos")
    @abstractmethod
    def registrarPago(pagoData:PagosEntity)->PagosEntity:
        pass
    @abstractmethod
    def registrarAbono(pagoData:PagosEntity)->PagosEntity:
        pass
    @abstractmethod
    def registroMultipago(pagoData:PagosEntity)->PagosEntity:
        pass