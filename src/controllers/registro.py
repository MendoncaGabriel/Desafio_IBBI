from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.registro import Registro
from src.models.produto import Produto
from src.schemas.registro import RegistroBase
from fastapi import HTTPException


def create_registro(db: Session, registro_data: RegistroBase) -> Registro:
    try:
        data_atual = datetime.now()

        # Buscar o produto associado ao registro
        produto = db.query(Produto).filter(Produto.id == registro_data.produto_id).first()
        if not produto:
            raise ValueError(f"Produto com ID {registro_data.produto_id} não encontrado.")

        # Verificar se a quantidade em estoque e suficiente para o registro
        if produto.quantidade < registro_data.quantidade:
            raise ValueError(f"Quantidade insuficiente no estoque para o produto {produto.id}.")

        # Incrementar o contador de vendas do produto
        produto.venda += 1
        db.commit()

        # Criar um novo registro
        novo_registro = Registro(
            observacao=registro_data.observacao,
            nome_cliente=registro_data.nome_cliente,
            usuario_id=registro_data.usuario_id,
            produto_id=registro_data.produto_id,
            data=data_atual
        )

        # Adicionar o novo registro ao banco de dados
        db.add(novo_registro)
        db.commit()
        db.refresh(novo_registro)

        return novo_registro

    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
