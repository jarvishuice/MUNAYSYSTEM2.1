from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reports.inventario.reportInventarioDAO import ReportInventarioDAO
from fastapi.responses import FileResponse

core= ReportInventarioDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
InventarioReport=APIRouter(prefix=f"{urlBase}/Reports/inventario", tags=["Reports"])
@InventarioReport.get("/{sede}")
async def reporteInventario(sede):
     trigger=core.generarReporte(sede)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'ReporteInventario{sede}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")