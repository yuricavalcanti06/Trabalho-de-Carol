
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
            pais = input("Digite o país de origem das receitas que deseja visualizar: ")
            receitas_do_pais = [receita for receita in lista_receitas if receita.paisdeorigem.lower() == pais.lower()]
            if len(receitas_do_pais) == 0:
                print(f"\nAinda não existem receitas cadastradas do país {pais}.")
            else:
                print("\nReceitas: ")
                print("-" * 30)
                for i, receita in enumerate(receitas_do_pais, start=1):
                    print(f"{i}. Nome da receita: {receita.nome}")
                    print(f"   País de origem: {receita.paisdeorigem}")
                    print(f"   Ingredientes: {receita.ingredientes}")
                    print(f"   Modo de preparo: {receita.mododepreparo}")
                    print("-" * 30)
        else:
            print("\nReceitas: ")
            print("-" * 30)
            for i, receita in enumerate(lista_receitas, start=1):
                print(f"{i}. Nome da receita: {receita.nome}")
                print(f"   País de origem: {receita.paisdeorigem}")
                print(f"   Ingredientes: {receita.ingredientes}")
                print(f"   Modo de preparo: {receita.mododepreparo}")
                print("-" * 30)
   
#-----------= Visualizar Favoritos =-----------#

def visualizar_favoritos(Receitas_Fav):
    os.system('cls')
    if len(Receitas_Fav) == 0:
        print("Ainda não existem receitas cadastradas nos favoritos")
    else:
        print("Favoritos:")
        print("-" * 30)
        for i, receita in enumerate(Receitas_Fav, start = 1):
            print(f"{i}. Nome da receita: {receita.nome}")
            print(f"   País de origem: {receita.paisdeorigem}")
            print(f"   Ingredientes: {receita.ingredientes}")
            print(f"   Modo de preparo: {receita.mododepreparo}")
            print("-" * 30)
            
#-----------= Favoritar Receita =-----------#

def favoritar_receita(lista_receitas):
    os.system('cls')
    if len(lista_receitas) == 0:
        print("\nAinda não existem receitas cadastradas.")
    else:
        visualizar_receitas(lista_receitas)
        indice = input("\nDigite o numero da receita que deseja favoritar: ")
        if indice.isdigit():
            indice = int(indice) - 1
            if indice >=0 and indice < len(lista_receitas):
                Receitas_Fav.append(lista_receitas[indice])
                print("\nReceita favoritada com sucesso!")
            else:
                print("\nÍndice inválido. Nenhuma receita foi favoritada.")
        else:
            print("\nEntrada inválida. Nenhuma receita foi favoritada.")

#-----------= Exlcuir dos Favoritos =-----------#

def excluir_favorito(Receitas_Fav):
    os.system('cls')
    if len(Receitas_Fav) == 0:
        print("\nAinda não existem receitas cadastradas nos favoritos.")
    else:
        visualizar_favoritos(Receitas_Fav)
        indice = input("\nDigite o número da receita que deseja excluir: ")
        if indice.isdigit():
            indice = int(indice) - 1
            if indice >=0 and indice < len(Receitas_Fav):
                del Receitas_Fav[indice]
                print("\nReceita excluída com sucesso!")
            else:
                print("\nÍndice inválido. Nenhuma receita foi excluída.")
        else:
            print("\nEntrada inválida. Nenhuma receita foi excluída.")

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
    print("7. Excluir dos Favoritos")
    print("8. Sair")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_receita(lista_receitas)
    elif opcao == "2":
        visualizar_receitas(lista_receitas)
    elif opcao == "3":
        atualizar_receita(lista_receitas)
    elif opcao == "4":
        excluir_receita(lista_receitas)
    elif opcao == "5":
        favoritar_receita(lista_receitas)
    elif opcao == "6":
        visualizar_favoritos(Receitas_Fav)
    elif opcao == "7":
        excluir_favorito(Receitas_Fav)
    elif opcao == "8":
        print("\nEncerrando o programa. Até mais!")
        print("-" * 30)
        break
    else:
        print("\nOpção inválida. Tente novamente.")
