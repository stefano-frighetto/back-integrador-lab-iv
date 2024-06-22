from fastapi import FastAPI, status, Query, File, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel,EmailStr,Field, SecretStr, PositiveInt, field_validator
from datetime import date
from typing import List, Optional, Annotated
from passlib.context import CryptContext
from fastapi import UploadFile
from fastapi.responses import FileResponse
import os
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import shutil
import secrets

usuario_router = APIRouter()

@usuario_router.get('/usuarios', tags=['Usuarios'], response_model=List[UsuarioBaseSchema], status_code=200)
def get_usuarios():
    db = Session()
    result = UsuarioService(db).get_usuarios()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@usuario_router.get('/usuarios/{id}', tags=['Usuarios'], response_model=[UsuarioBaseSchema])
def get_usuario(id: int):
    db = Session()
    try:
        result = UsuarioService(db).get_usuario(id)
        if not result:
            return JSONResponse(status_code=404, content={'message': "No encontrado"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    finally:
        db.close()

@usuario_router.post('/usuarios', tags=['Usuarios'], status_code=201)
def create_usuario(usuario: Usuario) :
    db = Session()    
    UsuarioService(db).create_usuario(usuario)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})

@usuario_router.put('/usuarios/{id}', tags=['Usuarios'], response_model=[UsuarioBaseSchema], status_code=200)
def update_usuario(id: int, usuario: Usuario):
    db = Session()
    result = UsuarioService(db).get_usuario(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    UsuarioService(db).update_usuario(id, usuario)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})

@usuario_router.delete('/usuarios/{id}', tags=['Usuarios'], response_model=[UsuarioBaseSchema], status_code=200)
def delete_usuario(id: int):
    db = Session()
    result: UsuarioModel = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    UsuarioService(db).delete_usuario(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})




