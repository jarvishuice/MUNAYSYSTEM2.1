from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.productos.productosDAO import ProductosDAO,ProductosEntity

from core.Implements.auth.authDAO import AuthDAO  #core de seguridad para validar tokens 
core= ProductosDAO()
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Productos=APIRouter(prefix=f"{urlBase}/Productos", tags=["Productos"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")


@Productos.post("/")
async def crearProductos(ProductoData:ProductosEntity,auten:str=Depends(aut))-> ProductosEntity:
   
    trigger=core.registrarProducto(ProductoData)
    
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Productos.get("/search/{name}")
async def buscarProducto(name,auten:str=Depends(aut)) -> list[ProductosEntity]:
    trigger=core.BuscarProducto(name)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@Productos.get('/filterCategoria/{categoria}/{sede}')
async def FiltroCategorias(categoria,sede,auten:str=Depends(aut)) -> list[ProductosEntity]: 
    trigger = core.ProductosByCategoriaandSede(categoria,sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
       


