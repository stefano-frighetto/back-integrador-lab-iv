from pydantic import BaseModel, Field
from datetime import date


class Inscripcion(BaseModel):
    id: int = Field (gt=0)
    evento_id: int = Field (gt=0)
    usuario_id: int = Field (gt=0)
    fecha_inscripción: date

