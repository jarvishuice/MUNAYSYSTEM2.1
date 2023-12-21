from pydantic import BaseModel
from typing import Optional

class ItemsInventarioEntity(BaseModel):
    id:Optional[int]
    nombre:str

    precio:float
    cantidad:int
    tipo:str
   