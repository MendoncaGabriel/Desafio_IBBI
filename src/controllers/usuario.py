from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate
import bcrypt
import jwt
import datetime

def signup(db: Session, usuario: UsuarioCreate):
    # Criptografar senha do usuario
    hash = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())
    
    usuario = Usuario(
        nome=usuario.nome,
        login=usuario.login,
        senha=hash.decode('utf-8'),
    )

    payload = {
        'usuario_id': usuario.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Expira em 1 dia
    }
    
    # não ta funcionando isto!!!!!
    token = "" #jwt.encode(payload, 'your_secret_key', algorithm='HS256').decode('utf-8')

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return {"usuario": usuario, "access_token": token}

