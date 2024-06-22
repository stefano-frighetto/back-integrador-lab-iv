from fastapi import Depends, FastAPI
from config.database import engine, Base
from routers.categoria_router import categoria_router
# from routers.usuario_router import usuario_router
from routers.evento_router import evento_router
# from routers.inscripcion_router import inscripcion_router
from config.database import Base, engine
from middleware.error_handler import ErrorHandler
from middleware.jwt_bearer import JWTBearer
from fastapi.staticfiles import StaticFiles


Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(JWTBearer())])
app.title = "Práctico nro 5"

app.add_middleware(ErrorHandler)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(categoria_router)
# app.include_router(usuario_router)
app.include_router(evento_router)
# app.include_router(inscripcion_router)

