from models.usuario_model import UsuarioModel
from schemas.usuario_schemas import UsuarioSchema,UsuarioBaseSchema
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
