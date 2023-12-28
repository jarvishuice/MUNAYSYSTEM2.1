
from typing import Annotated
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from controllers.api.router.Ordenes.OrdenesRouter import Ordenes
from controllers.api.router.clientes.clientesRouter import Clientes
from controllers.api.router.pedidos.pedidosRouter import Pedidos
from controllers.api.router.wallet.walletRouter import Wallet
from controllers.api.router.user.userRouter import usuarios
from controllers.api.router.loggin.logginRouter import Loggin
from controllers.api.router.pagos.PagosRouter import Pagos
from controllers.api.router.pagos.pagosWalletRouter import PagosWallet
from controllers.api.router.clientes.deudas.clientesDeudasRouter import DeudasClientes
from controllers.api.router.productos.productosRouter import Productos
from controllers.api.router.finance.tasaDollarRouter import TasaDollar
from controllers.api.router.planDeCuentas.planDeCuentasRouter import PlanCuentas
from controllers.api.router.reports.Inventario.reportInventarioRouter import InventarioReport
from controllers.api.router.reports.coffeshop.preccierreRouter import ReportPrecierre
from controllers.api.router.reports.coffeshop.cierreROUTER import ReportCierre
from controllers.api.router.reports.coffeshop.cierreROUTERByFECHA import ReportCierreF
from controllers.api.router.metrics.metricsRouter import Metric
from controllers.api.router.visitas.visitantesRouter import Visitantes
from controllers.api.router.visitas.visitasRouter import Visitas
from controllers.api.router.espacios.espaciosRouter import ESPACIOS
origins = ["*"]
autenticacion=OAuth2PasswordBearer(tokenUrl="token")


app =FastAPI(title="Nest Coworking",version="2.1",openapi_url="/localhost",logger="info",logs_paths="/home/munay/MUNAYSYSTEM2.1DAO/APP/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ESPACIOS)
app.include_router(Visitantes)
app.include_router(Visitas)
app.include_router(Ordenes)
app.include_router(Clientes)
app.include_router(Pedidos)
app.include_router(Wallet)
app.include_router(usuarios)
app.include_router(Loggin)
app.include_router(Pagos)
app.include_router(PagosWallet)
app.include_router(DeudasClientes)
app.include_router(Productos)
app.include_router(TasaDollar)
app.include_router(PlanCuentas)
app.include_router(InventarioReport)
app.include_router(ReportPrecierre)
app.include_router(ReportCierre)
app.include_router(ReportCierreF)
app.include_router(Metric)
@app.get("/MUNAY/nest/test")
async def test():
    return True
@app.get("/items/")
async def readToken(token:Annotated[str,Depends(autenticacion)]):
    return token    
