from passlib.context import CryptContext
from models.usuario_model import UsuarioModel
from schemas.usuario_schemas import UsuarioSchema,UsuarioBaseSchema
from utils.validators import idDuplicados,emailDuplicado

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService():
    def __init__(self, db) -> None:
        self.db = db

    def get_usuarios(self):
        result = self.db.query(UsuarioModel).all()
        return result
    
    def get_usuario(self, id):
        result = self.db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        return result
    
    def create_usuario(self, user: UsuarioSchema):
        lista = self.get_usuarios()
        idDuplicados(user, lista)
        emailDuplicado(user,lista)
        contrasenia_hasheada = pwd_context.hash(user.password)
        user.password = contrasenia_hasheada
        new_user = UsuarioModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return new_user
    ########### aca no se 
    def update_user(self, id: int, user: UsuarioSchema):
        result = self.db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        result.evento_id = user.evento_id
        result.usuario_id = user.usuario_id
        result.fecha_inscripción = user.fecha_inscripción
        self.db.commit()
        return result
    
    def delete_user(self, id:int):
        self.db.query(UsuarioModel).filter(UsuarioModel.id == id).delete()
        self.db.commit()
        return True