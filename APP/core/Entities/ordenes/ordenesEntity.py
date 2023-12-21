from pydantic import BaseModel
from typing import Optional

class OrdenesEntity(BaseModel):
    id:Optional[str]
    total:Optional[float]
    sede:str
    fechaPedido:Optional[str]
    fechapago:Optional[str]
    status:str
    idCliente:int
    tipoPago:Optional[str]
    idPago:Optional[str]
    
class OrdenesDetalladasEntity(BaseModel):
   idOrden:str
   cliente:str
   total:float
   fecha:str
   hora:str
   status:str                                       
    
    
