from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from controllers.api.router.espacios.clientes.clientesDeudasRouter import DEUDASCLIENTES
from controllers.api.router.espacios.pagos.pagosRouter import PAGOS
from controllers.api.router.espacios.productos.productosRouter import PRODUCTOS
from controllers.api.router.espacios.pedidos.pedidosRouter import Pedidos
from controllers.api.router.espacios.ordenes.ordenesRouter import Ordenes
from controllers.api.router.espacios.wallet.walletRouter import Wallet
from controllers.api.router.espacios.report.reportEspaciosRouter import ReporteEspacios
urlBase = "/MUNAY/nest/"
ESPACIOS=APIRouter(prefix=f"/MUNAY/nest/Espacios", tags=["ESPACIOS"])
ESPACIOS.include_router(Wallet)
ESPACIOS.include_router(PAGOS)
ESPACIOS.include_router(Ordenes)
ESPACIOS.include_router(Pedidos)
ESPACIOS.include_router(PRODUCTOS)
ESPACIOS.include_router(DEUDASCLIENTES)
ESPACIOS.include_router(ReporteEspacios)