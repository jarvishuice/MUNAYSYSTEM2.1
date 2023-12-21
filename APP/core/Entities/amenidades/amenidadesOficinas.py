from pydantic import BaseModel
from typing import Optional
class AmenidadOficina(BaseModel):
    idOficina:str
    idAmenidad:str
    cantidad:float