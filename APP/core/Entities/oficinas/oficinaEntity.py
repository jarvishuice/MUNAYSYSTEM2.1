from pydantic import BaseModel
from typing import Optional
class OficinaEntity(BaseModel):
    id: str
    capacidad: int
    idResponsable:int
    status:str
    precio: float
    sede: str
    fechaInicio:str
    fechaFin:str
    deposito:float
    fechaPago: str

        
        