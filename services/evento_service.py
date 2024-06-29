import shutil
from fastapi import File, UploadFile
from fastapi.responses import FileResponse
from models.evento_model import EventoModel
from schemas.evento_schema import EventoSchema
from utils.validators import idDuplicados


class EventoService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_eventos(self):
        result = self.db.query(EventoModel).all()
        return result
    
    def get_evento(self, id):
        result = self.db.query(EventoModel).filter(EventoModel.id == id).first()
        return result
    
    def create_evento(self, evento: EventoSchema):
        lista = self.get_eventos()
        idDuplicados(evento, lista)
        new_evento = EventoModel(**evento.model_dump())
        self.db.add(new_evento)
        self.db.commit()
        return new_evento
    
    def update_evento(self, id: int, evento: EventoSchema):
        result = self.db.query(EventoModel).filter(EventoModel.id == id).first()
        result.nombre = evento.nombre
        result.descripcion = evento.descripcion
        result.fecha_inicio = evento.fecha_inicio
        result.fecha_fin = evento.fecha_fin
        result.lugar=evento.lugar
        result.cupos=evento.cupos
        result.categoria_id=evento.categoria_id
        self.db.commit()
        return result
    
    def delete_evento(self, id:int):
        self.db.query(EventoModel).filter(EventoModel.id == id).delete()
        self.db.commit()
        return True
    
    def get_evento_categoria(self, idCategoria:int):
        result = self.db.query(EventoModel).filter(EventoModel.idCategoria == idCategoria).all()
        return result