from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.registro import Registro
from src.models.produto import Produto
from src.schemas.registro import RegistroEntrada
from fastapi import HTTPException

class DataHora:
    @staticmethod
    def data_atual():
        return datetime.now()
    
    @staticmethod
    def hora():
        return DataHora.data_atual().strftime("%H:%M")
    
    @staticmethod
    def data():
        return DataHora.data_atual().strftime("%d/%m/%Y")

def create(db: Session, registro: RegistroEntrada):
    try:
        # Buscar o produto associado ao registro
        produto = db.query(Produto).filter(Produto.id == registro.produto_id).first()
        if not produto:
            raise HTTPException(
                status_code=404, 
                detail=f"Produto com id: {registro.produto_id} não encontrado"
            )

        # Verificar se a quantidade em estoque é suficiente para o registro
        if produto.quantidade < registro.quantidade:
            raise HTTPException(
                status_code=409,
                detail=f"Quantidade insuficiente no estoque do produto {produto.descricao} id: {produto.id}."
            )

        # Incrementar o contador de vendas do produto
        produto.venda += 1
        
        # Decrementar estoque do produto
        produto.quantidade -= registro.quantidade
        db.commit()

        # Criar um novo registro
        data = DataHora.data()
        hora = DataHora.hora()
        
        novo_registro = Registro(
            data=data,
            hora=hora,
            produto_id=produto.id,
            descricao_produto=produto.descricao,
            nome_cliente=registro.nome_cliente,
            nome_vendedor=registro.nome_vendedor,
            observacao=registro.observacao,
            valor=float(produto.valor),
            total= round(produto.valor * registro.quantidade, 2),
            quantidade=registro.quantidade
        )

        db.add(novo_registro)
        db.commit()
        db.refresh(novo_registro)

        return novo_registro

    except SQLAlchemyError as error:
        db.rollback()
        print(error)
        raise HTTPException(status_code=500, detail="Erro interno do servidor: registro -> create") from error

def ultimas_vendas(db: Session, limit: int = 4):
    try:
        vendas = db.query(Registro).order_by(
            Registro.data.desc(), 
            Registro.hora.desc()
        ).limit(limit).all()
        
        return vendas
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: registro -> ultimas_vendas") from error

def get_by_id(db: Session, id: int):
    try:
        registro = (
            db.query(Registro)
            .filter(Registro.id == id)
            .first()
        )
        if not registro:
            raise HTTPException(status_code=404, detail=f"Registro dom id: {id} não encontrado")
        
        return registro
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: registro -> get_by_id") from error
    
def delete(db: Session, id: int):
    try:
        registro = db.query(Registro).filter(Registro.id == id).first()
        if not registro:
            raise HTTPException(
                status_code=404, 
                detail=f"Registro com id: {id} não encontrado para remoção"
            )
            
        db.delete(registro)
        db.commit()
        
        return registro
        
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: registro -> delete") from error
    