from pydantic import BaseModel
from typing import Optional

class PedidosEntity(BaseModel):
    idOrden:str
    idProducto:int
    cantidad:int
    total:float

    
class PedidoEspacioEntity(BaseModel):
    idOrden:str
    idProducto:str
    cantidad:float
    total:float

