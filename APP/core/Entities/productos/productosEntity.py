from pydantic import BaseModel
from typing import Optional

class ProductosEntity(BaseModel):
    id:Optional[int]
    nombre:str
    urlimagen:str
    precio:float
    cantidad:int
    tipo:str
    almacen:Optional[str]