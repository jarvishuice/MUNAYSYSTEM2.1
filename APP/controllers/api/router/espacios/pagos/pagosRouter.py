from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.pagos.pagosEspaciosDAO import PagosEspaciosDAO,PagosEntity

core= PagosEspaciosDAO()
urlBase = "/Pagos"
PAGOS=APIRouter(prefix=f"{urlBase}",tags=["PAGOS ESPACIOS"])
security = HTTPBearer()
validator=AuthDAO()
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")
@PAGOS.post("/")
async def RegistraPAgo(Pago:PagosEntity):
    
    trigger=core.registrarPago(Pago)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@PAGOS.post("/Abonos")
async def registrarAbono(Pago:PagosEntity,auten:str=Depends(aut))-> PagosEntity:
   trigger= core.registrarAbono(Pago)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])  
@PAGOS.post("/MultiPago")
async def registrarMultiPago(Pago:PagosEntity,auten:str=Depends(aut))-> PagosEntity:
   trigger= core.registroMultipago(Pago)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge']) 
