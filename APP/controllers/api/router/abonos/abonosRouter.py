""" 
Este es el procesador de pagos desde el api 
su implementacion puede variar dependiendo del entorno de produccion
"""
from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.Abonos.abonoDAO import AbonoDAO,AbonosEntity

core= AbonoDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
ABONOS=APIRouter(prefix=f"{urlBase}/Abonos", tags=["Abonos"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")

@ABONOS.post("/")
async def RegistraPAgo(Abono:AbonosEntity):#auten:str=Depends(aut)):
    
    trigger=core.registrarAbono(Abono)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@ABONOS.get("/{idCliente}/{sede}")
async def consulta(idCliente,sede):
    trigger=core.getAbono(idCliente,sede)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])