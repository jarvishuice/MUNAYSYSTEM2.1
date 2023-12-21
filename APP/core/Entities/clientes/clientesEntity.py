from pydantic import BaseModel
from typing import Optional



class ClientesEntity(BaseModel):
    id:Optional[int]
    nombre:str
    apellido:Optional[str]
    correo:str
    tlf:str
    fechaingreso:str
    fechacambio:Optional[str]
    codigo:Optional[int]
    credito:Optional[float]
    ci:str
    identificacion:str
    direccion:str
    deuda:Optional[float] 
    
