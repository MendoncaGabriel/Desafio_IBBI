import os
import jwt
import bcrypt
import datetime

SECRET_KEY = os.getenv("SECRET_KEY")
validade = 24

def gerarToken (usuario_id: int) -> str:
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=validade)  
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def chechToken(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        # Verifica a validade do token
        expiracao = datetime.datetime.fromtimestamp(payload['exp'])
        agora = datetime.datetime.now()

        if expiracao >= agora:
            return payload  
        else:
            return None  

    except jwt.ExpiredSignatureError:
        print("Token expirado")
        return None
    except jwt.InvalidTokenError:
        print("Token inválido")
        return None

def criptografar(texto: str) -> bytes:
    hashed = bcrypt.hashpw(texto.encode('utf-8'), bcrypt.gensalt())
    return hashed

def verificarSenha(texto: str, hashed: bytes) -> bool:
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')  # Garante que hashed seja bytes

    return bcrypt.checkpw(texto.encode('utf-8'), hashed)
