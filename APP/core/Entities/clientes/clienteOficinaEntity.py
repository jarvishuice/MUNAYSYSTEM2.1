
from pydantic import BaseModel
from typing import Optional

class ClientesOficinaEntity(BaseModel):
    idCliente:int
    idOficina:str
    status:str
    
class ClienteOficinaEntityDetail(BaseModel):
    idCliente:int 
    nombre:str
    ci:str
    idOficina:str
    