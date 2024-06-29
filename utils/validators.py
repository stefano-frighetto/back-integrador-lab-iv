from fastapi.exceptions import HTTPException
from typing import List

def idDuplicados(obj, lista:List):
        for item in lista:
            if item.id == obj.id :
                raise HTTPException(status_code=409,
                            detail=f"El id ya se encuentra registrado" )
            
def emailDuplicado(obj, lista:List):
        for item in lista:
            if item.email == obj.email:
                raise HTTPException(status_code=409,
                            detail=f"El email ya se encuentra registrado" )