from sqlalchemy.orm import Session
from src.models.usuario import Usuario
import bcrypt
import jwt
import datetime
from fastapi import HTTPException
from src.schemas.usuario import UsuarioBase, UsuarioToken

SECRET_KEY = 'your_secret_key'

def signup(db: Session, usuario: UsuarioBase):
    # Verificar se o login já existe
    db_usuario = db.query(Usuario).filter(Usuario.login == usuario.login).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Login already registered")

    # Criptografar a senha do usuário
    hash_senha = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())

    # Criar novo usuário no banco de dados
    novo_usuario = Usuario(
        nome=usuario.nome,
        login=usuario.login,
        senha=hash_senha.decode('utf-8'),
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    # Gerar token JWT
    token = generate_jwt_token(novo_usuario.id)

    # Retornar dados do usuário e token JWT usando o esquema UsuarioToken
    return UsuarioToken(id=novo_usuario.id, nome=novo_usuario.nome, login=novo_usuario.login, token=token)

def generate_jwt_token(usuario_id: int) -> str:
    # Gerar token JWT com o ID do usuário
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Expira em 1 dia
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
