from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reports.coffeshop.cierreDAO import ReportCierreDAO
from fastapi.responses import FileResponse

core= ReportCierreDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
ReportCierre=APIRouter(prefix=f"{urlBase}/Reports/coffeshop/cierre", tags=["Reports"])
@ReportCierre.get("/{sede}")
async def reporteInventario(sede):
     trigger=core.generarCierre(sede)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'CierreDeJornada{sede}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")