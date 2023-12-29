from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.clientes.deudaClientesEspaciosDAO import DeudaCientesEspaciosDAO
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Entities.clientes.deudaClienteCoffeShopEntitity import DeudaClienteCoffeShopEntity,DetalleDedudaClientesEntity
from core.Entities.pagos.pagosEntity import PagosEntity
from core.Implements.auth.authDAO import AuthDAO
core= DeudaCientesEspaciosDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/deudas"
DEUDASCLIENTES=APIRouter(prefix=f"{urlBase}/Deudas", tags=["DEUDAS ESPACIOS"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="Erro de autenticacion ")
   

@DEUDASCLIENTES.get("/{sede}")
async def deudasCleintes(sede:str)->list[DeudaClienteCoffeShopEntity]: 
  
    trigger=core.getDeudasClientesBySede(sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@DEUDASCLIENTES.get("/{sede}/{idCliente}")
async def detallesDeudasClientes(sede:str,idCliente:int)->list[DetalleDedudaClientesEntity]:
    trigger=any
    respuesta=any
    trigger=core.getDetalleDeudaClienteBySede(sede,idCliente)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@DEUDASCLIENTES.put("/cerrarDeudas/{Rwallet}/{Dwallet}")
async def cerrarDeudasClientes(Rwallet,Dwallet,pago:PagosEntity):
   trigger=core.closeDeudaClientBySede(pago,float(Rwallet),float(Dwallet))
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])