import time
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.wallet.walletDAO import WalletDAO
from core.Entities.wallet.walletEntity import WalletEntity
from core.Implements.auth.authDAO import AuthDAO  #core de seguridad para validar tokens 
core= WalletDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Wallet=APIRouter(prefix=f"{urlBase}/Wallet", tags=["Wallet"])

def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")

@Wallet.get("/consultaSaldo/{idCliente}")
async def consultaSaldo(idCliente:int):
   
    trigger=core.consultaSaldo(idCliente)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   
@Wallet.post("/Descuento/" )
async def descuentoWallet(wallet:WalletEntity,auten:str=Depends(aut)):
    
    trigger=core.descuentowallet(wallet)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Wallet.post("/Recarga/")
async def RecargaWallet(wallet:WalletEntity):
    
    trigger=core.reacargarWallet(wallet)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])