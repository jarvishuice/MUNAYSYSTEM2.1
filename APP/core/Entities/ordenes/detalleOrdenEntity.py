from pydantic import BaseModel
from typing import Optional

class DetalleOrdenesEntity(BaseModel):
    id:str
    nombre:str
    cantidad:float
    total:float
class OrdenDetalladaEntity(BaseModel):
    nombre :str
    cantidad:float
    precio:float
    total:float


    