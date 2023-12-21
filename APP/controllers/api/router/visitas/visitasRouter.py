from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.Visitas.VisitasDAO import VisitasDao,VisitasEntity

from core.Implements.auth.authDAO import AuthDAO
core= VisitasDao()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Visitas=APIRouter(prefix=f"{urlBase}/Visitas", tags=["Visitas"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="Erro de autenticacion ")
   

@Visitas.post("/Reg/Visita")
async def crearVisita(Visita:VisitasEntity,auten:str=Depends(aut)):
  
    trigger=core.crearVisita(Visita)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   
@Visitas.put("/salida/{idVisita}/")
async def salidaVisita(idVisita,auten:str=Depends(aut)):
   trigger=core.salidaVisita(idVisita)
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Visitas.get("/vistasToday/{sede}")
async def visitasToday(sede:str ,auten:str=Depends(aut)):
    trigger=core.getAllVisitasDay(sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Visitas.get("/visitasByMotivo/{sede}/{motivo}")
async def getAllVisitasBymotivo(sede,motivo)->list[VisitasEntity]:
   trigger=core.getFilterByMotivoAndSede(motivo,sede)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Visitas.get("/visitasBystatus/{sede}/{status}")
async def getAllVisitasBystatus(sede,status)->list[VisitasEntity]:
   trigger=core.getVisitasByStatus(sede,status)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Visitas.get("/visitas/detail/today/{sede}")
async def getDetailViistasTodayBysede(sede):
   """
    Retrieves the details of visits for a given location for the current day.

    Args:
        sede (str): The location for which visit details are requested.

    Returns:
        dict: The visit details for the given location and current day.

    Raises:
        HTTPException: If there is an error, with a status code of 400 and an error message.
    """
   trigger=core.getVisitasDetailToday(sede)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
      
       raise HTTPException(400,trigger['mesagge'])