from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import SessionLocal
from src.controllers import usuario as usuario_controller
from src.schemas.usuario import UsuarioCreate, UsuarioSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model= UsuarioCreate)
def signup (usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_controller.signup(db, usuario)