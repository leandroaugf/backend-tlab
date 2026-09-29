import random;
import string;

from sqlalchemy import Column, Float, ForeignKey, Integer, String;

from app.database import Base;

def gerar_id_ponto(tamanho: int = 7) -> str:
    caracteres = string.ascii_lowercase + string.digits
    return "".join(random.choices(caracteres, k=tamanho));

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String, nullable=False)

class Ponto(Base):
    __tablename__ = "pontos"

    id = Column(String, primary_key=True, default=gerar_id_ponto)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    descricao = Column(String, nullable=False, default="sem descrição")

