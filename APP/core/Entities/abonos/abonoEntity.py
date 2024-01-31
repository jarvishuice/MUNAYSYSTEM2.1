from pydantic import BaseModel
class AbonosEntity(BaseModel):
    id:str
    idCliente:int
    idPago:str
    status:str
    monto:float
    sede:str
    