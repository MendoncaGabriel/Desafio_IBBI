from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from fastapi import HTTPException
from src.schemas.usuario import UsuarioBase, UsuarioToken, UsuarioLoginSaida
from src.utilities.auth import gerarToken, criptografar, chechToken, verificarSenha

def signup(db: Session, usuario: UsuarioBase):
    # Verificar se o login já existe
    db_usuario = db.query(Usuario).filter(Usuario.login == usuario.login).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Login já cadastrado")

    hash_senha = criptografar(usuario.senha)

    # Criar novo usuário no banco de dados
    novo_usuario = Usuario(
        nome=usuario.nome,
        login=usuario.login,
        senha=hash_senha.decode('utf-8'),
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    token = gerarToken(novo_usuario.id)

    return UsuarioToken(id=novo_usuario.id, nome=novo_usuario.nome, login=novo_usuario.login, token=token)


def login(db: Session, usuario: UsuarioBase):
    # Verificar se usuário existe
    db_usuario = db.query(Usuario).filter(Usuario.login == usuario.login).first()
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Usuário não existe")
    
    # Verificar se senha está correta
    senha_correta = verificarSenha(usuario.senha, db_usuario.senha)
    if not senha_correta:
        raise HTTPException(status_code=401, detail="Senha incorreta!")
    
    # Gerar token de autenticação
    token = gerarToken(db_usuario.id)

    return UsuarioLoginSaida(login=db_usuario.login, token=token)

