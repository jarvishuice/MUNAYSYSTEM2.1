from pydantic import BaseModel
from typing import Optional
class WalletEntity(BaseModel):
    id:Optional[str]
    idcliente: int
    monto: float
    idpago:str
    status:str
    