from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reports.espacios.cierreDAO import ReportCierreDAO
from core.Implements.reports.espacios.cierreMensualDAO import ReportCierreMensualDAO
from fastapi.responses import FileResponse
core= ReportCierreDAO()
coreMensual= ReportCierreMensualDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/Report"
ReporteEspacios=APIRouter(prefix=f"{urlBase}", tags=["Reports Espacios"])
@ReporteEspacios.get("/{sede}")
async def reporteCierre(sede):
     trigger=core.generarCierre(sede)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'ReporteEspaciosCierre{sede}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")
@ReporteEspacios.get("/Mensual/{sede}/{mes}/{year}")
async def reporteMensual(sede,mes,year):
     trigger=coreMensual.generarCierre(sede,mes,year)
     archivo =trigger['response']
     if trigger['status']==True:
        archivo=trigger['response']
        return FileResponse(path=archivo,media_type='application/pdf', filename=f'ReporteMensualEspacios{mes}-{year}{sede}.pdf')
     else:
         raise HTTPException(400,f"{trigger['mesagge']}")