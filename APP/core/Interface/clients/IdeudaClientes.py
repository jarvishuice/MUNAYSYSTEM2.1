from core.Entities.clientes.deudaClienteCoffeShopEntitity import DeudaClienteCoffeShopEntity ,DetalleDedudaClientesEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
from core.Entities.pagos.pagosEntity import PagosEntity

class IDedudaClientes(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IClientes")
    
    @abstractmethod
    def getDeudasClientesBySede(sede)->list[DeudaClienteCoffeShopEntity]:
        pass
    @abstractmethod
    def getDetalleDeudaClienteBySede(sede)->list[DetalleDedudaClientesEntity]:
        pass
    @abstractmethod
    def closeDeudaClientBySede(pago:PagosEntity,Dwallet:float,RWallet:float)->PagosEntity:
        pass
    @abstractmethod
    def __statusByDeudabyClientebySede__(idPago:str,sede:str,idCliente:int):
        pass

        