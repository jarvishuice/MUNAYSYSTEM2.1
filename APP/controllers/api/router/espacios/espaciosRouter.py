from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from controllers.api.router.espacios.pedidos.pedidosRouter import Pedidos
from controllers.api.router.espacios.ordenes.ordenesRouter import Ordenes
urlBase = "/MUNAY/nest/"
ESPACIOS=APIRouter(prefix=f"/MUNAY/nest/Espacios", tags=["ESPACIOS"])
ESPACIOS.include_router(Ordenes)
ESPACIOS.include_router(Pedidos)