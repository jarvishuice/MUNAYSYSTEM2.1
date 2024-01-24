from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.finance.tasaDollarDAO import TasaDollarDAO,TasaDollarEntity

core= TasaDollarDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
TasaDollar=APIRouter(prefix=f"{urlBase}/finance", tags=["tasaDollar"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")

""""
hay que descomentar la linea para aplicar la autenticacion
"""

   
@TasaDollar.get("/tasaDollarLast")
async def getTAsaDollar(auten:str=Depends(aut)):
   trigger=core.tasaDollarLastRegister()
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@TasaDollar.post("/")
async def updateTasa() -> TasaDollarEntity|bool :
   trigger = core.updateTasa()
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
   