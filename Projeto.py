class Receita:
    def __init__(self):
        self.nome = ""
        self.paisdeorigem = ""
        self.ingredientes = ""
        self.mododepreparo = ""

#-----------= Cadastro =---------#
def cadastrar_receita(lista_receitas):
    os.system('cls')
    receita = Receita()
    receita.nome = input("\nDigite o nome da receita: ")
    receita.paisdeorigem = input("Digite o país de origem: ")
    receita.ingredientes = input("Digite os ingredientes: ")
    receita.mododepreparo = input("Digite o modo de preparo: ")
    lista_receitas.append(receita)
    print("\nReceita cadastrada com sucesso!")
    
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
        visualiar_favoritos(Receitas_Fav)
    elif opcao == "7":
        print("\nEncerrando o programa. Até mais!")
        break
