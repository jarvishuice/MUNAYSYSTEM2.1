from pydantic import BaseModel
from typing import Optional
from core.Entities.ordenes.ordenesEntity import OrdenesEntity
from core.Entities.pedidos.pedidosEntity import PedidosEntity
from core.Entities.pagos.pagosEntity import PagosEntity
class MasterOrdenEntity(BaseModel):
   orden=OrdenesEntity()
   pedido=list[PedidosEntity]
   pago=Optional[PagosEntity]
    