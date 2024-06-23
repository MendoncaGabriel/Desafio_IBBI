from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
import src.controllers.registro as registro_controller
from src.schemas.registro import RegistroBase, RegistroSchema
from src.utilities.auth import checkAuthorization

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/")
def create (registro: RegistroBase, db: Session = Depends(get_db)):
    return registro_controller.create(db, registro)
