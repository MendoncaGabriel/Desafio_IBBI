from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from src.controllers import usuario as usuario_controller
from src.schemas.usuario import UsuarioBase, UsuarioToken, UsuarioLoginSaida, UsuarioLoginEntrada

router = APIRouter()
        
@router.post("/signup", response_model= UsuarioToken)
def signup (usuario: UsuarioBase, db: Session = Depends(get_db)):
    return usuario_controller.signup(db, usuario)

@router.post("/login", response_model=UsuarioLoginSaida)
def login (usuario: UsuarioLoginEntrada, db: Session = Depends(get_db)):
    return usuario_controller.login(db, usuario)