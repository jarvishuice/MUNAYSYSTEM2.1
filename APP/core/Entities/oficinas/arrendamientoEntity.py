from pydantic import BaseModel
from typing import Optional
from Entity.clienteOficinaEntity import ClientesOficinaEntity
from Entity.contratoOficinasEntity import ContratoOficinaEntity
from Entity.historicoOcupanteEntity import HistoricoOcupantesEntity

class ArrendamientoEntity(BaseModel):
    ocupantes:list[ClientesOficinaEntity]
    contrato:ContratoOficinaEntity
