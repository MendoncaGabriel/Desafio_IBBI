from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioBase, UsuarioToken, UsuarioLoginSaida
from src.utilities.auth import gerarToken, criptografar, verificarSenha


def signup(db: Session, usuario: UsuarioBase) -> UsuarioToken:
    try:
        # Verificar se o login ja existe
        if db.query(Usuario).filter(Usuario.login == usuario.login).first():
            raise HTTPException(status_code=400, detail="Login já cadastrado")

        # Criptografar a senha do usuario
        hash_senha = criptografar(usuario.senha)

        # Criar novo usuario no banco de dados
        novo_usuario = Usuario(
            nome=usuario.nome,
            login=usuario.login,
            senha=hash_senha.decode('utf-8'),
        )

        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        # Gerar token de autenticacao para o novo usuario
        token = gerarToken(novo_usuario.id)

        return UsuarioToken(id=novo_usuario.id, nome=novo_usuario.nome, login=novo_usuario.login, token=token)
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error


def login(db: Session, usuario: UsuarioBase) -> UsuarioLoginSaida:
    try:
        # Verificar se usuario existe
        db_usuario = db.query(Usuario).filter(Usuario.login == usuario.login).first()
        if not db_usuario:
            raise HTTPException(status_code=400, detail="Usuário não existe")
        
        # Verificar se a senha esta correta
        if not verificarSenha(usuario.senha, db_usuario.senha):
            raise HTTPException(status_code=401, detail="Senha incorreta!")
        
        # Gerar token de autenticacao
        token = gerarToken(db_usuario.id)

        return UsuarioLoginSaida(login=db_usuario.login, token=token)

    except Exception as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
