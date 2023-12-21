from pydantic import BaseModel
from typing import Optional
class ConsumoAmenidadEntity(BaseModel):
    id:str
    idAmenidad:str
    idOficina:str
    sede:str
    fechaConsumo:str
    cantidad:float
    idCliente:int
class ConsumoAmenidadesDetallesEntity(BaseModel):
    id:str
    idAmenidad:str
    idOficina:str
    sede:str
    fechaConsumo:str
    cantidad:float
    idCliente:int
    nombreCliente:str