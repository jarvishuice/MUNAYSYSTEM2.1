from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.planDeCuenta.planDeCuentaDAO import PlanDeCuentaDAO,PlanDeCuentaEntity

from core.Implements.auth.authDAO import AuthDAO  #core de seguridad para validar tokens 
core= PlanDeCuentaDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
PlanCuentas=APIRouter(prefix=f"{urlBase}/Cuentas", tags=["Cuentas"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")



@PlanCuentas.get("/{sede}")
async def buscarProducto(sede,auten:str=Depends(aut)) -> list[PlanDeCuentaEntity]:
    trigger=core.getFormPayBySede(sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])



