from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from core.Implements.user.userDAO import UserDAO
from core.Entities.user.usersEntity import UsersEntity
core= UserDAO()

urlBase = "/MUNAY/nest"
usuarios=APIRouter(prefix=f"{urlBase}/User", tags=["User"])

@usuarios.post("/")
async def crearUsuario(User:UsersEntity):

    trigger=core.crearUser(User)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@usuarios.get("/{username}") #hay que borrar este end point porqu ees para probar la funcion 
async def BuscarUsuario(username:str)-> UsersEntity:
    trigger=core.busquedaUsuario(username)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@usuarios.put("/status/{status}/")
async def ActualizarStatusUser(status,credential:UsersEntity):
   trigger=core.cambiarEstatus(credential,status)
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
   