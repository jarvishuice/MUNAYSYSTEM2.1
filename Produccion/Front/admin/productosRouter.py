from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.ordenes.ordenesEspaciosDAO import OrdenesEspaciosDAO
from core.Implements.productos.productosEspaciosDAO import ProductosEspaciosDAO,ProductosEntity
core= ProductosEspaciosDAO()
urlBase = "/Productos"
PRODUCTOS=APIRouter(prefix=f"{urlBase}",tags=["PRODUCTOS ESPACIOS"])
security = HTTPBearer()
validator=AuthDAO()
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")

@PRODUCTOS.post("/")
async def crearProductos(ProductoData:ProductosEntity)->ProductosEntity:
    trigger= core.registrarProducto(ProductoData)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])

@PRODUCTOS.get("/search/{name}/{sede}")
async def buscarProducto(name:str,sede:str) -> list[ProductosEntity]:
    trigger=core.BuscarProducto(name,sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
@PRODUCTOS.get("/filterCategoria/{categoria}/{sede}")
async def FiltroCategorias(categoria,sede) -> list[ProductosEntity]: 
    trigger = core.ProductosByCategoriaandSede(categoria,sede)
    if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
    else:
       raise HTTPException(400,trigger['mesagge'])
       