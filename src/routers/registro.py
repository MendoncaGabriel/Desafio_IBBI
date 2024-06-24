from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from src.controllers  import registro as Controller
from src.schemas.registro import RegistroEntrada, RegistroSaida
from src.utilities.auth import checkAuthorization
from typing import List

router = APIRouter()
        
@router.post("/", response_model=RegistroSaida)
def create (
    registro: RegistroEntrada, 
    db: Session = Depends(get_db),
    security: dict = Depends(checkAuthorization)
):
    return Controller.create(db, registro)


@router.get("/ultimas-vendas", response_model=List[RegistroSaida])
def get_ultimas_vendas(
    db: Session = Depends(get_db),
    security: dict = Depends(checkAuthorization)
):
    return Controller.ultimas_vendas(db)


@router.get("/{id}", response_model=RegistroSaida)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
    security: dict = Depends(checkAuthorization)
):
    return Controller.get_by_id(db, id)


@router.delete("/{id}", response_model=RegistroSaida)
def delete(
    id: int,
    db: Session = Depends(get_db),
    security: dict = Depends(checkAuthorization)
):
    return  Controller.delete(db, id)