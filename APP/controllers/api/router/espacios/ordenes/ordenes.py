from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
urlBase = "/MUNAY/nest/Espacios"
Ordenes=APIRouter(prefix=f"/MUNAY/nest/Espacios/Ordenes", tags=["Ordenes"])
@Ordenes.get("/heloo")
def hello():
    return {"hello"}
