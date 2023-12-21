from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.clientes.clientesDAO import ClientesDAO
from core.Entities.clientes.clientesEntity import ClientesEntity
from core.Implements.auth.authDAO import AuthDAO
core= ClientesDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Clientes=APIRouter(prefix=f"{urlBase}/Clientes", tags=["Clientes"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="Erro de autenticacion ")
   

@Clientes.post("/")
async def CrearCliente(ClienteDATA:ClientesEntity,auten:str=Depends(aut)):
  
    trigger=core.crearCliente(ClienteDATA)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   
@Clientes.get("/total/")
async def clientesCOunt(auten:str=Depends(aut)):
   trigger=core.contarClientes()
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Clientes.get("/search/{nombre}")
async def BuscarClientes(nombre ,auten:str=Depends(aut)):
    trigger=core.buscarClientes(nombre)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Clientes.get("/getall/")
async def readAllCLientes()->list[ClientesEntity]|list:
   trigger=core.getAllClientes()    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Clientes.put("/update")
async  def UpdateClient(cliente:ClientesEntity)->ClientesEntity:
   """
    Update a client's information in the database.

    Args:
        cliente (ClientesEntity): An instance of the ClientesEntity class representing the updated client information.

    Returns:
        ClientesEntity: The updated client information, represented by an instance of the ClientesEntity class.

    Raises:
        HTTPException: If the update fails, an HTTPException is raised with a 400 status code and the error message.
    """
   trigger=core.editCliente(cliente)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])