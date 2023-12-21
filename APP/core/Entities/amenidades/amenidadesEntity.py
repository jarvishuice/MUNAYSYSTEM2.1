from pydantic import BaseModel
from typing import Optional

class AmenidadEntity(BaseModel):
    idProducto:str
    cantidad:float
    status:str
    id:str
    
class AmenidadesNombre(BaseModel):
    idProducto:str
    cantidad:float
    status:str
    id:str
    nombreProducto:str
    