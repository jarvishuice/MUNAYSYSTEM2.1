from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.clientes.deudaClientesDAO import DeudaCientesDAO
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Entities.clientes.deudaClienteCoffeShopEntitity import DeudaClienteCoffeShopEntity,DetalleDedudaClientesEntity
from core.Entities.pagos.pagosEntity import PagosEntity
from core.Implements.auth.authDAO import AuthDAO
core= DeudaCientesDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
DeudasClientes=APIRouter(prefix=f"{urlBase}/Clientes/Deudas", tags=["Clientes"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="Erro de autenticacion ")
   

@DeudasClientes.get("/{sede}")

async def deudasCleintes(sede:str,auten:str=Depends(aut))->list[DeudaClienteCoffeShopEntity]: 
  
    trigger=core.getDeudasClientesBySede(sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@DeudasClientes.get("/{sede}/{idCliente}")
async def detallesDeudasClientes(sede:str,idCliente:int,auten:str=Depends(aut))->list[DetalleDedudaClientesEntity]:
    trigger=any
    respuesta=any
    trigger=core.getDetalleDeudaClienteBySede(sede,idCliente)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@DeudasClientes.put("/cerrarDeudas/{Rwallet}/{Dwallet}")
async def cerrarDeudasClientes(Rwallet,Dwallet,pago:PagosEntity):
   trigger=core.closeDeudaClientBySede(pago,float(Rwallet),float(Dwallet))
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])