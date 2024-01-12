from pydantic import BaseModel
from typing import Optional

class PagosEntity(BaseModel):
    id:str
    fecha:Optional[str]
    monto:float
    motivo:str
    idcliente:int
    idformadepago:int
    referencia:str
    idtaza:Optional[str]
    sede:Optional[str]

    
class PagosEntity(BaseModel):
    id:str
    fecha:str
    monto:float
    motivo:str
    cliente:str
    formaDepago:str
    referencia:str
    tasa:float
    sede:str