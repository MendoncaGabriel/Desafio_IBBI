from sqlalchemy.orm import Session
from src.models.registro import Registro
from src.models.produto import Produto
from src.schemas.registro import RegistroBase
from datetime import datetime
from typing import List
from sqlalchemy import func

def create(db: Session, registro_data: RegistroBase):
    data_atual = datetime.now()
    
    # Incrementar venda no produto!!!
    
    data = Registro(
        observacao=registro_data.observacao,
        nome_cliente=registro_data.nome_cliente,
        usuario_id=registro_data.usuario_id,
        produto_id=registro_data.produto_id,
        data=data_atual
    )
    
    db.add(data)
    db.commit()
    db.refresh(data)
    
    return data 