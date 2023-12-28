from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response

from core.Implements.pedidos.pedidosEspaciosDAO import PedidosEspaciosDAO,PedidosEntity
urlBase = "/MUNAY/nest/Espacios"
Pedidos=APIRouter(prefix=f"{urlBase}",tags=["PEDIDOS ESPACIOS"])
core=PedidosEspaciosDAO()
@Pedidos.post("/")
async def regPedido(pedido:PedidosEntity)->PedidosEntity:
    trigger=core.crearPedido(pedido)
    if trigger['status'] ==True:
        respuesta= trigger['response']
        return respuesta
    else:
        raise HTTPException(400,trigger['mesagge'])