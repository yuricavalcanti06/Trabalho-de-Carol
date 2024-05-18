
import os

#-----------= Funções do codigo(inicio) =-----------#

class Receita:
    def __init__(self):
        self.nome = ""
        self.paisdeorigem = ""
        self.ingredientes = ""
        self.mododepreparo = ""

#-----------= Cadastro =-----------#

def cadastrar_receita(lista_receitas):
    os.system('cls')
    receita = Receita()
    receita.nome = input("\nDigite o nome da receita: ")
    receita.paisdeorigem = input("Digite o país de origem: ")
    receita.ingredientes = input("Digite os ingredientes: ")
    receita.mododepreparo = input("Digite o modo de preparo: ")
    lista_receitas.append(receita)
    print("\nReceita cadastrada com sucesso!")
    
#-----------= Visualização =-----------#

def visualizar_receitas(lista_receitas):
    os.system('cls')
    if len(lista_receitas) == 0:
        print("\nAinda não existem receitas cadastradas.")
    else:
        filtrar_pais = input("Deseja filtrar as receitas por país? (s/n): ")
        if filtrar_pais.lower() == 's':
            pais = input("Digite o país de origem das receitas que deseja visualizar: ") #TRY EXCEPT?
            receitas_do_pais = [receita for receita in lista_receitas if receita.paisdeorigem.lower() == pais.lower()]
            if len(receitas_do_pais) == 0:
                print(f"\nAinda não existem receitas cadastradas do país {pais}.")
            else:
                for i, receita in enumerate(receitas_do_pais, start=1):
                    print(f"{i}. Nome da receita: {receita.nome}")
                    print(f"   País de origem: {receita.paisdeorigem}")
                    print(f"   Ingredientes: {receita.ingredientes}")
                    print(f"   Modo de preparo: {receita.mododepreparo}")
                    print("-" * 30)
        else:
            for i, receita in enumerate(lista_receitas, start=1):
                print(f"{i}. Nome da receita: {receita.nome}")
                print(f"   País de origem: {receita.paisdeorigem}")
                print(f"   Ingredientes: {receita.ingredientes}")
                print(f"   Modo de preparo: {receita.mododepreparo}")
                print("-" * 30)
                    
#-----------= Visualizar Favoritos =-----------#

def visualisar_favoritos(lista_receitas):
    os.system('cls')
    if len(Receitas_Fav) == 0:
        print("Ainda não existem receitas cadastradas nos favoritos")
    else:
        print("Favoritos:")
        for i, receita in enumerate(Receitas_Fav, start = 1):
            print(f"{i}. Nome da receita: {receita.nome}")
            print(f"   País de origem: {receita.paisdeorigem}")
            print(f"   Ingredientes: {receita.ingredientes}")
            print(f"   Modo de preparo: {receita.mododepreparo}")
            print("-" * 30)
            
#-----------= Funções do codigo(Fim) =-----------#
    
#-----------= Listas =---------------#

lista_receitas = []
Receitas_Fav = []

#----------= Começo do código =-----------#

while True:
    print("\nMenu:")
    print("1. Cadastrar receita")
    print("2. Visualizar receitas")
    print("3. Atualizar receita")
    print("4. Excluir receita")
    print("5. Favoritar receita")
    print("6. Visualizar Favoritos")
    print("7. Sair")
    
    opcao = input("\nDigite o número da opção desejada: ")
    
    if opcao == "1":
        cadastrar_receita(lista_receitas)
    elif opcao == "2":
        lista_receitas = []
        visualizar_receitas(lista_receitas)
    elif opcao == "3":
        lista_receitas = []
        atualizar_receita(lista_receitas)
    elif opcao == "4":
        lista_receitas = []
        excluir_receita(lista_receitas)
    elif opcao == "5":
        favoritar_receita(lista_receitas)
    elif opcao == "6":
        Receitas_Fav = []
        visualisar_favoritos(Receitas_Fav)
    elif opcao == "7":
        print("\nEncerrando o programa. Até mais!")
        break



