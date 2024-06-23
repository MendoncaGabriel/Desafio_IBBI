from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from src.controllers.registro  import create
from src.schemas.registro import RegistroEntrada, RegistroSaida
from src.utilities.auth import checkAuthorization

router = APIRouter()
        
@router.post("/", response_model=RegistroSaida)
def create (
    registro: RegistroEntrada, 
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)

):
    return create(db, registro)