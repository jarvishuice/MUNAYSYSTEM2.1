from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reports.coffeshop.precierreDAO import ReportPreCierreDAO
from fastapi.responses import FileResponse

core= ReportPreCierreDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
ReportPrecierre=APIRouter(prefix=f"{urlBase}/Reports/coffeshop/precierre", tags=["Reports"])
@ReportPrecierre.get("/{sede}")
async def reporteInventario(sede):
     trigger=core.generarPrecierre(sede)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'ReportePrecierre{sede}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")