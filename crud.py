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
        print("1- Adicionar Produto\n" "2- Excluir Produto\n" "3- Ver tabela\n" "4- Modificar Tabela")
        
        resposta = int(input("O que você deseja fazer?\n"))

        if resposta == 1:
            criar_produto()
            break
        elif resposta == 2:
            excluir_produto()
            break
        elif resposta == 3:
            Ver_Tabela_Menu()
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
    produto_existente = Session.query(Lojinha).filter_by(nome_produto=nome_produto).first()

    if produto_existente:
        print("Já temos um Produto com este Nome")
        menu_repetir()
        
    quant = int(input("Quanto você quer adicionar?"))
    preco = float(input("Qual o preço do seu produto?"))
    marca = str(input("E qual marca deseja adicionar?"))
    novo_produto = Lojinha(nome_produto=nome_produto, quant=quant, preco=preco,marca=marca)
    Session.add(novo_produto)
    Session.commit()
    menu_repetir()

#DELETE
def excluir_produto():
    print("Aqui está a tabela de Produtos")
    Ver_Tabela()

    id_produto = str(input("Qual produto deseja excluir?"))

    produto = Session.query(Lojinha).filter_by(id_produto=id_produto).first()
    
    if produto:
        Session.delete(produto)
        Session.commit()
        print(f"Produto Número: {id_produto} foi deletado com sucesso!")
    else:
        print(f"Não existe nenhum produto com este nome...")
    menu_repetir()

#READ
def Ver_Tabela():
    produtos = Session.query(Lojinha).all()

    if produtos:
        print("Aqui Estão Seus Produtos:")
    for produto in produtos:
        print(f"ID: {produto.id} Nome:{produto.nome_produto} Quantidade:{produto.quant} Preço:R${produto.preco} Marca:{produto.marca}")
    else:
        print("Não Existem Produtos Adiconados")
    

def Ver_Tabela_Menu():
    Ver_Tabela()
    menu_repetir()

#UPDATE
def Modificar_tb():
        nome_antigo = str(input("Oque Deseja Modificar?"))
        produto = Session.query(Lojinha).filter_by(nome_produto = nome_antigo).first()

        if not produto:
            print("Produto Não Encontrado")
            return

        print(f"Produto Encontrado: Nome:{produto.nome_produto} Quantidade:{produto.quant} Preço:R${produto.preco} Marca:{produto.marca}")
        print("Oque Deseja Modificar?")
        print("[1] Nome [2]Quantidade [3]Preço [4]Marca [5]Todos")

        opcao_escolhida = int(input(""))

        if opcao_escolhida == 1:
            novo_nome = str(input("Insira um Novo Nome: "))
            produto.nome_produto = novo_nome
        elif opcao_escolhida == 2:
            nova_quantia = int(input("Informe a Nova Quantia: "))
            produto.quant = nova_quantia
        elif opcao_escolhida == 3:
            novo_preco = float(input("Informe o Novo Preço: "))
            produto.preco = novo_preco
        elif opcao_escolhida == 4:
            nova_marca = str(input("Informe a Nova Marca: "))
            produto.marca = nova_marca
        elif opcao_escolhida == 5:
            novo_nome = produto.nome_produto = str(input("Nome: "))
            nova_quantia = produto.quant = int(input("Quantidade: "))
            novo_preco = produto.preco = float(input("Preço: "))
            nova_marca = produto.marca =str(input("Marca: "))
        else:
            print("Opção Inválida")
            return
        
        Session.commit()
        print("Produto Adiconado com Sucesso!")
    
        menu_repetir()

def menu_repetir():
    while True:
        resposta = int(input("Você Deseja fazer mais alguma coisa? [1]sim [2]não "))

        if resposta == 1:
            menu()
            break
        elif resposta == 2:
            print("Saindo..........")
            break
        else:
            print("Opção Invalida")
menu()

