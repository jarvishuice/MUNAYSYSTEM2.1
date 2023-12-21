from pydantic import BaseModel
from typing import Optional



class LoginEntity(BaseModel):
    
    nombreUsuario:str
    password:str
    token:Optional[str]
    