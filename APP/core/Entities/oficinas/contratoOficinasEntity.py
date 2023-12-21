
from pydantic import BaseModel
from typing import Optional

class ContratoOficinaEntity(BaseModel):
    id:Optional[str]
    idOficina:str
    fechaInicio:Optional[str]
    fechaFinal:Optional[str]
    idResponsable:int
    sede:str
    fechaPago:Optional[str]