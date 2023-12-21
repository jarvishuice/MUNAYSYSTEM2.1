
from pydantic import BaseModel
from typing import Optional

class HistoricoOcupantesEntity(BaseModel):
    idContrato:str
    idCliente:int
    idOficina:str