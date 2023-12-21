from core.Implements.auth.authDAO import AuthDAO
from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.metric.coffeshop.CoffeshopMetricDAO import CoffeshopMetricDAO,CoffeshopMetrictEntity


core= CoffeshopMetricDAO() #DAO DEL CAFETING 
security = HTTPBearer()
validator=AuthDAO()
urlBase = "/MUNAY/nest"
Metric=APIRouter(prefix=f"{urlBase}/metric", tags=["metric"])
def aut(credendentials:HTTPAuthorizationCredentials= Depends(security)):
   token= credendentials.credentials
   validacion=validator.validarToken(token)
   if validacion['response']  == True:
      return True
   else:
     raise HTTPException(401,detail="token inauorizado ")



   
@Metric.get("/coffeshop/{sede}")
async def metricasCafetinBysede(sede,auten:str=Depends(aut)):
   trigger=core.ExtraerMetricasBysede(sede)
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])
@Metric.get("/coffeshop/global")
async def metricasGlobal(auten:str=Depends(aut)):
   trigger=core.ExtraerMetricasGlobal()
    
   if trigger['status'] ==True:
       respuesta= trigger['response']
       return respuesta
   else:
       raise HTTPException(400,trigger['mesagge'])


