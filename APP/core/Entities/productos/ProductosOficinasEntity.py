from pydantic import BaseModel
from typing import Optional
class productosOficinasEntity(BaseModel):
    id:str
    nombre:str
    urlimg:str
    precio:float
    cantidad:float
    tipo:str
    almacen:str
    sede:str
