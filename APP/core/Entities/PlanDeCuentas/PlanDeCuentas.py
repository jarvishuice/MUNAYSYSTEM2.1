from pydantic import BaseModel
from typing import Optional

class PlanDeCuentaEntity(BaseModel):
 id:int
 banco:str
 nCuenta:str
 metodo:str
 sede:str