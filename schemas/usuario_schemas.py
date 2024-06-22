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


class Usuario(BaseModel):
    id: PositiveInt =Field(gt=0,le=1000)
    nombre:str = Field (min_length=8, max_length=50)  
    email: EmailStr
    password: SecretStr = Field(min_length=8) 
    rol:str