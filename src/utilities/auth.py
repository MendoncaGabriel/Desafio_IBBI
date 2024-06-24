import os
import jwt
import bcrypt
import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, Security
from datetime import datetime, timedelta, timezone


SECRET_KEY = os.getenv("SECRET_KEY")
validade = 24
security = HTTPBearer()

def gerarToken(usuario_id: int) -> str:
    # Define o payload do token JWT
    expiracao = datetime.now(timezone.utc) + timedelta(hours=validade)
    payload = {
        'usuario_id': usuario_id,
        'exp': expiracao  
    }
    
    # Gera o token JWT com base no payload e na SECRET_KEY
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token

def checkAuthorization(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expiracao_timestamp = payload['exp']
        expiracao = datetime.fromtimestamp(expiracao_timestamp, tz=timezone.utc)
        agora = datetime.now(timezone.utc)

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
