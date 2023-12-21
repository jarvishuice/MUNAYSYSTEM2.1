from pydantic import BaseModel
from typing import Optional



class UsersEntity(BaseModel):
    id:Optional[int]
    nombre:str
    apellido:str
    ci:str
    nombreusuario:str
    password:str
    token:str
    status:str
    tipoUsuario:Optional[int]
    urlImagen:Optional[str]