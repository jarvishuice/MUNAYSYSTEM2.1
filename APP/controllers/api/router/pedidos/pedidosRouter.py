from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.pedidos.pedidosDAO import PedidosDAO
from core.Entities.pedidos.pedidosEntity import PedidosEntity
from core.Implements.auth.authDAO import AuthDAO  #core de seguridad para validar tokens 
core= PedidosDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Pedidos=APIRouter(prefix=f"{urlBase}/Pedidos", tags=["Pedidos"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")


@Pedidos.post("/")
async def crearPedidos(pedidosData:PedidosEntity,sede:str,auten:str=Depends(aut)):
   
    trigger=core.crearPedido(pedidosData,sede)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   


