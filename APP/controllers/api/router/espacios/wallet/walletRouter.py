import time
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.wallet.walletEspaciosDAO import WalletEspaciosDAO
from core.Entities.wallet.walletEntity import WalletEntity
from core.Implements.auth.authDAO import AuthDAO  #core de seguridad para validar tokens 
core= WalletEspaciosDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/Wallet"
Wallet=APIRouter(prefix=f"{urlBase}", tags=["WALLET ESPACIOS"])

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