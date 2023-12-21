from pydantic import BaseModel
from typing import Optional
from core.Entities.ordenes.ordenesEntity import OrdenesEntity
class DeudaClienteCoffeShopEntity(BaseModel):
    idCliente:str
    ci:str
    nombre:str
    cantidadOrdenes:int
    deuda:float

class DetalleDedudaClientesEntity(BaseModel):
    fechaPedido:str   
    producto:str
    cantidad:float
    precio: float
    total:str
    sede:str
    idOrden:str