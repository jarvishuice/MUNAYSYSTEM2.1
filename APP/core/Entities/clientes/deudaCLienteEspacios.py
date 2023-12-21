from pydantic import BaseModel
from typing import Optional
class DeudaClienteEspacios(BaseModel):
    idCliente:str
    nombre:str
    cantidadOrdenes:int
    deuda:float