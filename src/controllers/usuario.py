from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate

def signup (db: Session, usuario: UsuarioCreate):
    data = Usuario(**usuario.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
    return(data)

def login (db: Session, usuario: UsuarioCreate):


