from core.Entities.productos.productosEntity import ProductosEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IProductos(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IPagos")
    @abstractmethod
    def registrarProducto(productoData:ProductosEntity)->ProductosEntity:
        pass
    @abstractmethod
    def BuscarProducto(name:str)->list[ProductosEntity]:
        pass
    @abstractmethod
    def ProductosByCategoriaandSede(categoria:str,sede:str)->ProductosEntity:
        pass