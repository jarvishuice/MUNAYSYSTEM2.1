from core.Entities.productos.productosEntity import ProductosEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IProductos(ABC):
    """
    Autor: Jarvis Huice
    Fecha de Emisión: 29 de Diciembre, 2023

    Esta es una clase abstracta llamada IProductos que define la interfaz para las operaciones de productos.
    """

    def __init__(self):
        Logs.WirterTask("new implement IPagos")
    @abstractmethod
    def registrarProducto(productoData:ProductosEntity)->ProductosEntity:
        """
        Método abstracto para registrar un producto.

        Parámetros:
            productoData (ProductosEntity): La entidad del producto que se va a registrar.

        Retorna:
            ProductosEntity: La entidad del producto registrado.
        """
        pass
    @abstractmethod
    def BuscarProducto(name:str)->list[ProductosEntity]:
        """
        Método abstracto para buscar un producto por nombre.

        Parámetros:
        name (str): El nombre del producto a buscar.

        Retorna:
        list[ProductosEntity]: Una lista de entidades de productos que coinciden con el nombre proporcionado.
        """
        pass
    @abstractmethod
    def ProductosByCategoriaandSede(categoria:str,sede:str)->ProductosEntity:
        """
        Método abstracto para buscar productos por categoría y sede.

        Parámetros:
        categoria (str): La categoría de los productos a buscar.
        sede (str): La sede donde buscar los productos.

        Retorna:
        ProductosEntity: La entidad del producto que coincide con la categoría y sede proporcionadas.
        """
        pass