class Receita:
    def __init__(self):
        self.nome = ""
        self.paisdeorigem = ""
        self.ingredientes = ""
        self.mododepreparo = ""

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