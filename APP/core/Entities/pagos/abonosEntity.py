from pydantic import BaseModel
from typing import Optional



class AbonosEntity(BaseModel):
    id:Optional[str]
    idCliente:int
    idPago:str
    status:str
    monto:float
    
