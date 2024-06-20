import os
import jwt
import bcrypt
import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, Security


SECRET_KEY = os.getenv("SECRET_KEY")
validade = 24
security = HTTPBearer()

def gerarToken (usuario_id: int) -> str:
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=validade)  
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def checkAuthorization(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expiracao = datetime.datetime.fromtimestamp(payload['exp'])
        agora = datetime.datetime.now()

        if expiracao >= agora:
            return payload
        else:
            raise HTTPException(status_code=401, detail="Autorização expirada")

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Autorização expirada")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Autorização inválida")


def criptografar(texto: str) -> bytes:
    hashed = bcrypt.hashpw(texto.encode('utf-8'), bcrypt.gensalt())
    return hashed

def verificarSenha(texto: str, hashed: bytes) -> bool:
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8') 
    return bcrypt.checkpw(texto.encode('utf-8'), hashed)
