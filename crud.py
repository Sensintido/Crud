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

def menu():
    while True:
        print("1- Adicionar Produto" \
            "2-Excluir Produto" \
            "3-Atualizar tabela" \
            "4-Modificar Tabela")
        
        resposta = int(input("O que você deseja fazer?"))

        if resposta == 1:
            criar_produto()
            break
        elif resposta == 2:
            excluir_produto()
            break
        elif resposta == 3:
            Atualizar_tb()
            break
        elif resposta == 4:
            Modificar_tb()
            break
        else:
            print("Você Não Digitou Nenhuma Opção Permitida!!!")
        return

#CREAT
def criar_produto():
    nome_produto = str(input("Qual o nome do seu produto?"))
    quant = int(input("Quanto você quer adicionar?"))
    preco = float(input("Qual o preço do seu produto?"))
    marca = str(input("E qual marca deseja adicionar?"))

    novo_produto = Lojinha(nome_produto=nome_produto, quant=quant, preco=preco,marca=marca)

    Session.add(novo_produto)
    Session.commit()

#DELETE
def excluir_produto():
    nome_produto = str(input("Qual produto deseja excluir?"))
    
    produto = Session.query(Lojinha).filter_by(nome_produto=nome_produto).first()
    if produto:
        Session.delete(produto)
        Session.commit()
        print(f"{nome_produto} foi deletado com sucesso!")
    else:
        print(f"Não existe nenhum produto com este nome...")