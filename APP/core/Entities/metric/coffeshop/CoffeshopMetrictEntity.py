from pydantic import BaseModel
from typing import Optional

class CoffeshopMetrictEntity(BaseModel):
    ventasDiarias:float
    ventasMensual:float
    deudas:float
    