from core.Entities.user.usersEntity import UsersEntity
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from core.Implements.login.loginDAO import LogginDAO
from core.Entities.user.loginEntity import LoginEntity
core= LogginDAO()

urlBase = "/MUNAY/nest"
Loggin=APIRouter(prefix=f"{urlBase}/Loggin", tags=["Loggin"])

@Loggin.post("/")
async def IniciarSeccion(Loggin:LoginEntity):
    
    trigger=core.IniciarSeccion(Loggin)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Loggin.post("/logout/")
def Logout(user:UsersEntity):
    trigger=core.cerrarSeccion(user)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
   