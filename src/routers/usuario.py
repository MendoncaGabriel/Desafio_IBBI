from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from src.controllers import usuario as Controller
from src.schemas.usuario import UsuarioEntrada, UsuarioSaida, UsuarioLogin, UsuarioRemove
router = APIRouter()
        
@router.post("/signup", response_model=UsuarioSaida)
def signup (
    usuario: UsuarioEntrada, 
    db: Session = Depends(get_db)
):
    return Controller.signup(db, usuario)

@router.post("/login", response_model=UsuarioSaida)
def login (
    usuario: UsuarioLogin, 
    db: Session = Depends(get_db)
):
    return Controller.login(db, usuario)

@router.delete("/{id}", response_model=UsuarioRemove)
def delete(
    id: int,
    usuario: UsuarioLogin, 
    db: Session = Depends(get_db)
):
    return Controller.delete(db, usuario, id)
    