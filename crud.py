from sqlalchemy import create_engine, Column, Integer, Numeric, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///banco.db", echo=True)
Session = sessionmaker(bind=db)
Session = Session() #fazer quests
Base = declarative_base()

class Lojinha(Base):
    __tablename__ = "Lojinha"

    id = Column(Integer, primary_key= True, autoincrement= True)
    nome_produto = Column(String, nullable=False)
    quant = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    marca = Column(String, nullable=False)

Base.metadata.create_all(db)
