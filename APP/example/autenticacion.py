from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

app = FastAPI()
security = HTTPBearer()

# Verificar si el token es válido y corresponde a un usuario autenticado
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        # Aquí puedes realizar cualquier verificación adicional, como consultar la base de datos para asegurarte de que el token corresponde a un usuario válido
        user = payload["username"]
        return user
    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Token inválido")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

# Ruta protegida que requiere autenticación
@app.get("/ruta_protegida")
def ruta_protegida(current_user: str = Depends(get_current_user)):
    return {"message": f"Hola, {current_user}. Esta es una ruta protegida."}

# Ruta para iniciar sesión y generar el token
@app.post("/login")
def login(username: str, password: str):
    # Aquí puedes realizar la autenticación del usuario y verificar las credenciales
    # Si las credenciales son válidas, genera un token y devuélvelo al cliente
    token = jwt.encode({"username": username}, "secret_key", algorithm="HS256")
    return {"token": token}
