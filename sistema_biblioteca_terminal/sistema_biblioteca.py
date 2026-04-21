#BIBLIOTECAS
import csv
import os

#VARIAVEL GLOBAL
ARQUIVO = "livros.csv"

# Criar arquivo se não existir
def inicializar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "titulo", "autor", "status"])


#CREATE

def gerar_id():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                return 1
            return int (reader[-1][0]) + 1
    except:
        1

def cadastrar_livro(): 
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    id_livro = gerar_id()

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([id_livro, titulo, autor, "Disponivel" ])

    print("Livro cadastrado com sucesso!")

# Função para listar todos os livros cadastrados
def listar_livros():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print(linha)



def menu(): 
    # while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Emprestar/Devolver livro")
    print("4 - Remover livro")
    print("0 - Sair")

    # Variavel que recebe opcao de escolha do usuario
    opcao = input("Escolha: ")
    print ("Opção escolhida:",opcao)

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    
inicializar_arquivo()    
menu()
