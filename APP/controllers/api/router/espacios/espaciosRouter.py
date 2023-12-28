from fastapi import APIRouter, FastAPI,Request,HTTPException,UploadFile,File,Response
from controllers.api.router.espacios.ordenes.ordenes import Ordenes
urlBase = "/MUNAY/nest/Espacios"
espacios=FastAPI(title="Nest Coworking",version="2.1",openapi_url="/localhost",logger="info",logs_paths="/home/munay/MUNAYSYSTEM2.1DAO/APP/")
espacios=APIRouter(prefix=f"{urlBase}", tags=["espacios"])
espacios.add_route(Ordenes)