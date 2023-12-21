""" 
Este es el procesador de pagos desde el api 
su implementacion puede variar dependiendo del entorno de produccion
"""
from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.pagos.pagosWalletDAO import PagosWalletDAO
from core.Entities.pagos.pagosEntity import PagosEntity
core= PagosWalletDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
PagosWallet=APIRouter(prefix=f"{urlBase}/PagosWallet", tags=["Pagos Wallet"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")

@PagosWallet.post("/")
async def COnsumoWallet(Pago:PagosEntity,auten:str=Depends(aut)):
    
    trigger=core.registrarPagoConWallet(Pago)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@PagosWallet.post("/REcargaWallet")
async def RecargaWallet(pago:PagosEntity,auten:str=Depends(aut))-> PagosEntity:
   trigger= core.RecargarWallet(pago)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
   

