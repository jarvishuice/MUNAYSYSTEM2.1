from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.visitantes.visitantesDAO import VisitantesDAO
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Implements.auth.authDAO import AuthDAO
core= VisitantesDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Visitantes=APIRouter(prefix=f"{urlBase}/Visitas", tags=["Visitas"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="Erro de autenticacion ")
   

@Visitantes.post("/")
async def crearVisitante(ClienteDATA:ClientesEntity,auten:str=Depends(aut)):
  
    trigger=core.crearVisitante(ClienteDATA)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   
@Visitantes.get("/total/")
async def contarVisitantes(auten:str=Depends(aut)):
   trigger=core.contarVisitante()
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Visitantes.get("/search/{ci}")
async def BuscarVisitantes(ci ,auten:str=Depends(aut)):
    trigger=core.buscarVisitante(ci)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Visitantes.get("/getAll/Visitantes")
async def getAllVisitor()->list[ClientesEntity]:
   trigger=core.getAllVisitantes()
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])