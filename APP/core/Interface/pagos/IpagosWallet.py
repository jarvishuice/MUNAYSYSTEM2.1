from core.Entities.pagos.pagosEntity import PagosEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IPagosWallet(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IPagos")
    @abstractmethod
    def registrarPagoConWallet(pagoData:PagosEntity)->PagosEntity:
        pass
    @abstractmethod
    def RecargarWallet(pagosData:PagosEntity)->PagosEntity:
        pass