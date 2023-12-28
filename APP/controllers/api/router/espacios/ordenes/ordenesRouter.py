from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.ordenes.ordenesEspaciosDAO import OrdenesEspaciosDAO
from core.Entities.ordenes.ordenesEntity import OrdenesEntity,OrdenesDetalladasEntity
from core.Entities.pedidos.pedidosEntity import PedidosEntity
core= OrdenesEspaciosDAO()
urlBase = "/Ordenes"
Ordenes=APIRouter(prefix=f"{urlBase}",tags=["ORDENES ESPACIOS"])
security = HTTPBearer()
validator=AuthDAO()
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")
@Ordenes.get("/")
def hello():
    return {"hello"}
@Ordenes.post("/")
async def crearOrden(ordenData:OrdenesEntity,pedido:list[PedidosEntity]): 

    datos=ordenData
    trigger=core.crearOrden(datos,pedido)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.get("/{sede}")
async def ordenesAbiertas(sede,auten:str=Depends(aut)):
   trigger=core.OrdenesPorPagarBysede(sede)
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.get("/{status}/{sede}")
async def  ordenesByStatusAndSede(status,sede,auten:str=Depends(aut)):
   trigger=core.OrdenesFilterByStatusAndSede(status,sede)
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.post("/today/today/{sede}")
async def OrdenesDeldia(sede:str):
   trigger=core.OrdenesDeLajornada(sede)
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.post("/DETALLE/{idOrden}")
async def DEtalleOrdenesById(idOrden:str):
    trigger=core.getDetailOrden(idOrden)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.post("/filter/sede/{sede}")
async def getOrdenesBysede(sede)->list[OrdenesDetalladasEntity]:
   trigger=core.getOrdenesBysede(sede)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Ordenes.put("/delete/{idOrden}")
async def deleteOrder(idOrden)-> bool:
    trigger=core.deleteOrder(idOrden)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
    
