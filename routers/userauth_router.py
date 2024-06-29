from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.userauth_schema import UsuarioAuth

userauth_router = APIRouter()

@userauth_router.post('/login', tags=['Auth'])
def login(user: UsuarioAuth):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)