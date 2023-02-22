from sqlalchemy import Column, Integer, String, Float

from core.configs import settings

class ProdutoModel(settings.DBBaseModel):
    __tablename__: str = 'produtos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    imagem: str = Column(String(100)) # 1000x1000