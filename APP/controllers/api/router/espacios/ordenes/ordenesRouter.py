from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
urlBase = "/MUNAY/nest"
Ordenes=APIRouter(prefix=f"{urlBase}",)
@Ordenes.get("/")
def hello():
    return {"hello"}
