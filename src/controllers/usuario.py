# src/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate, UsuarioSchema
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError

router = APIRouter()

SECRET_KEY = "coloque_uma_chave_secreta_aqui"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/signup", response_model=UsuarioSchema)
def signup(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(usuario.senha)
    db_usuario = Usuario(nome=usuario.nome, login=usuario.login, senha=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.post("/login")
def login(usuario: UsuarioBase, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.login == usuario.login).first()
    if not db_usuario or not verify_password(usuario.senha, db_usuario.senha):
        raise HTTPException(status_code=401, detail="Login ou senha incorretos")
    
    access_token_expires = timedelta(ACCESS_TOKEN_EXPIRE_DAYS=1)
    access_token = create_access_token(
        data={"sub": db_usuario.login}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
