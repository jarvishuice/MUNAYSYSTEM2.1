from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reports.coffeshop.cierreByFechaDAO import ReportCierreByFechaDAO
from fastapi.responses import FileResponse

core= ReportCierreByFechaDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
ReportCierreF=APIRouter(prefix=f"{urlBase}/Reports/coffeshop/cierreByFecha", tags=["Reports"])
@ReportCierreF.get("/{sede}")
async def reporteInventario(sede,ano,mes,day):
     trigger=core.generarCierre(sede,ano,mes,day)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'CierreDeJornada{sede}:{ano}-{mes}-{day}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")