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

# Atualiza dados do livro
def atualizar_status():
    id_busca = input("Digite o ID do livro: ")
    linhas = []
 
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        linhas = list(reader)
 
    for i in range(1, len(linhas)):
        if linhas[i][0] == id_busca:
            if linhas[i][3] == "Disponivel":
                linhas[i][3] = "Emprestado"
            else:
                linhas[i][3] = "Disponivel"
            print("Status atualizado!")
            break
    else:
        print("Livro não encontrado.")
 
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(linhas)

def remover_livro():
    id_busca = input("Digite o ID do livro para remover: ")
    novas_linhas = []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            if linha[0] != id_busca:
                novas_linhas.append(linha)

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(novas_linhas)

    print("Livro removido (se existia).")
        

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
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        remover_livro()    
    
inicializar_arquivo()    
menu()
