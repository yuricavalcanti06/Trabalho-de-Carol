
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
#--------= Atualização de receita =--------#
def atualizar_receita(lista_receitas):
    os.system('cls')
    if len(lista_receitas) == 0:
        print("\nAinda não existem receitas cadastradas.")
    else:
        visualizar_receitas(lista_receitas)
        try:
            indice = input("\nDigite o número da receita que deseja atualizar: ")
        except ValueError:
            print("\nEntrada inválida. Nenhuma receita foi atualizada")
        else:
            if indice.isdigit():
                indice = int(indice) - 1
                if 0 <= indice < len(lista_receitas):
                    receita = lista_receitas[indice]
                    receita.nome = input("Digite o novo nome da receita: ")
                    receita.paisdeorigem = input("Digite o novo país de origem: ")
                    receita.ingredientes = input("Digite os novos ingredientes: ")
                    receita.mododepreparo = input(
                        "Digite o novo modo de preparo: ")
                    print("\nReceita atualizada com sucesso!")
                else:
                    print("\nÍndice inválido. Nenhuma receita foi atualizada.")
#--------= Excluir =----------#
def excluir_receita(lista_receitas):
    os.system('cls')
    if len(lista_receitas) == 0:
        print("\nAinda não existem receitas cadastradas.")
    else:
        visualizar_receitas(lista_receitas)
        try:
            indice = input("\nDigite o número da receita que deseja excluir: ")
        except ValueError:
            print("Entrada inválida. Nenhuma receita foi excluída")
        else:
            if indice.isdigit():
                indice = int(indice) - 1
                if 0 <= indice < len(lista_receitas):
                    del lista_receitas[indice]
                    print("\nReceita excluída com sucesso!")
                else:
                    print("\nÍndice inválido. Nenhuma receita foi excluída.")
   
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
        try:
            indice = input("\nDigite o numero da receita que deseja favoritar: ")
        except ValueError:
            print("Valor inserido para favoritar é inválido, nenhuma receita foi favoritada")
        else:
            if indice.isdigit():
                indice = int(indice) - 1
                if indice >=0 and indice < len(lista_receitas):
                    Receitas_Fav.append(lista_receitas[indice])
                    print("\nReceita favoritada com sucesso!")
                else:
                    print("\nÍndice inválido. Nenhuma receita foi favoritada.")

#-----------= Exlcuir dos Favoritos =-----------#

def excluir_favorito(Receitas_Fav):
    os.system('cls')
    if len(Receitas_Fav) == 0:
        print("\nAinda não existem receitas cadastradas nos favoritos.")
    else:
        visualizar_favoritos(Receitas_Fav)
        try:
            indice = input("\nDigite o número da receita que deseja excluir: ")
        except ValueError:
            print("Entrada inválida. Nenhuma receita foi excluída")
        else:
            if indice.isdigit():
                indice = int(indice) - 1
                if indice >=0 and indice < len(Receitas_Fav):
                    del Receitas_Fav[indice]
                    print("\nReceita excluída com sucesso!")
                else:
                    print("\nÍndice inválido. Nenhuma receita foi excluída.")

#---------= Função representadora do os.remove() =---------#
def limparArquivo():
      #if os.path.exists("receita.txt"):
        #   os.remove("receita.txt")
     file = open("receita.txt" , "w")
     file.write("")
     file.close()
def limparArquivo2():
      #if os.path.exists("receita.txt"):
        #   os.remove("receita.txt")
     file = open("favoritos.txt" , "w")
     file.write("")
     file.close()
#---------= Adicionar e Ler o arquivo txt
def incluirRegistroArquivoReceita(lista_receitas): #SOLUÇÃO PARA O FAVORITOS N SALVAR
    file = open("receita.txt" , "a")
    texto = ""
    for receita in lista_receitas:
        texto += receita.nome +";"+receita.paisdeorigem+";"+receita.ingredientes+";"+receita.mododepreparo+">"
    
    file.write(texto)
    file.close()    
    
def incluirRegistroArquivoReceita2(lista_receitas): #SOLUÇÃO PARA O FAVORITOS N SALVAR
    file = open("favoritos.txt" , "a")
    texto = ""
    for receita in lista_receitas:
        texto += receita.nome +";"+receita.paisdeorigem+";"+receita.ingredientes+";"+receita.mododepreparo+">"
    
    file.write(texto)
    file.close()

def lerRegistrosArquivoReceita(lista_receitas):
    try:
        file = open("receita.txt" , "r")
    except:
        print("Erro: Receita não existe")
        return
    else:
        for linha in file.readlines():
            array_linha = linha.split(">")
            for coluna in array_linha:
                array_coluna = coluna.split(";")
                receita = Receita()
                if len(array_coluna) > 1: 
                   receita.nome = array_coluna[0]
                   receita.paisdeorigem = array_coluna[1]
                   receita.ingredientes = array_coluna[2]
                   receita.mododepreparo = array_coluna[3]
                   lista_receitas.append(receita) 
           
        file.close()    
def lerRegistrosArquivoReceita2(Receitas_Fav):
    try:
        file = open("favoritos.txt" , "r")
    except:
        print("Erro: Receita de favoritos não existe")
        return
    else:
        for linha in file.readlines():
            array_linha = linha.split(">")
            for coluna in array_linha:
                array_coluna = coluna.split(";")
                receita = Receita()
                if len(array_coluna) > 1: 
                   receita.nome = array_coluna[0]
                   receita.paisdeorigem = array_coluna[1]
                   receita.ingredientes = array_coluna[2]
                   receita.mododepreparo = array_coluna[3]
                   Receitas_Fav.append(receita) 
           
        file.close()    
#-----------= sugestão de receita =-----------#
def gerar_numero_aleatorio(tamanho_lista):
    global contador 
    contador += 1
    return contador % tamanho_ lista

def sugerir_receita_aleatoria(lista_receitas):
    if len(lista_receitas) += 0:
        print("\nAinda não existem receitas cadastradas.")
    else:
        indice_aleatorio = gerar_numero.aleatorio(len(lista_receitas))
        receita = lista_receitas[indice_aleatorio]
        print("\nSugestão de Receita:")
        print(f"Nome da receita: {receita.nome}")
        print(f"Pais de origem: {receita.paisdeorigem}")
        print(f"Ingredientes: {receita.ingredientes}")
        print(f"Modo de preparo: {receita.mododepreparo}")
    
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
    print("8. Sugerir Receita Aleatória")
    print("9. Sair")
    try:
        opcao = input("\nDigite o número da opção desejada: ")
    except ValueError:
        print("\nOpção inválida. Tente novamente.")
    else:
        if opcao == "1":
            cadastrar_receita(lista_receitas)
            limparArquivo()
            incluirRegistroArquivoReceita(lista_receitas)
        elif opcao == "2":
            lista_receitas = []
            lerRegistrosArquivoReceita(lista_receitas)
            visualizar_receitas(lista_receitas)
        elif opcao == "3":
            lista_receitas = []
            lerRegistrosArquivoReceita(lista_receitas)
            limparArquivo()
            atualizar_receita(lista_receitas)
            incluirRegistroArquivoReceita(lista_receitas)  
        elif opcao == "4":
            lista_receitas = []
            lerRegistrosArquivoReceita(lista_receitas)
            excluir_receita(lista_receitas)
            limparArquivo()
            incluirRegistroArquivoReceita(lista_receitas)
        elif opcao == "5":
            lista_receitas = []
            lerRegistrosArquivoReceita(lista_receitas)
            Receitas_Fav = []
            lerRegistrosArquivoReceita2(Receitas_Fav)
            limparArquivo2()
            favoritar_receita(lista_receitas)
            incluirRegistroArquivoReceita2(Receitas_Fav)
        elif opcao == "6":
            Receitas_Fav = []
            lerRegistrosArquivoReceita2(Receitas_Fav) 
            visualizar_favoritos(Receitas_Fav)
        elif opcao == "7":
            excluir_favorito(Receitas_Fav)
            limparArquivo2()
            incluirRegistroArquivoReceita2(Receitas_Fav)
        elif opcao == "8":
            lista_receitas = []
            lerRegistrosArquivoReceita(lista_receitas)
            sugerir_receita_aleatoria(lista_receitas)
        elif opcao == "9":
            print("\nEncerrando o programa. Até mais!")
            print("-" * 30)
            break
