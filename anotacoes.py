# ==========================================
# FUNÇÃO HASH POR SOMA DOS CARACTERES
# ==========================================

def hash_soma(chave, tamanho):
    soma = 0

    for caractere in chave:
        soma += ord(caractere)

    return soma % tamanho


# ==========================================
# FUNÇÃO HASH POLINOMIAL INCREMENTAL
# ==========================================

def hash_polinomial(chave, tamanho):
    base = 31
    valor_hash = 0

    for caractere in chave:
        valor_hash = (valor_hash * base + ord(caractere)) % tamanho

    return valor_hash


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

tamanho = 10

while True:
    print("\n===== MENU =====")
    print("1 - Hash por soma dos caracteres")
    print("2 - Hash polinomial incremental")
    print("3 - Testar os dois métodos")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    elif opcao == "1":
        chave = input("Digite a chave: ")

        indice = hash_soma(chave, tamanho)

        print("Índice gerado:", indice)

    elif opcao == "2":
        chave = input("Digite a chave: ")

        indice = hash_polinomial(chave, tamanho)

        print("Índice gerado:", indice)

    elif opcao == "3":
        chave = input("Digite a chave: ")

        indice_soma = hash_soma(chave, tamanho)
        indice_polinomial = hash_polinomial(chave, tamanho)

        print("\nChave:", chave)
        print("Hash por soma:", indice_soma)
        print("Hash polinomial:", indice_polinomial)

    else:
        print("Opção inválida!")






#         def hash_soma(chave, tamanho):
#     soma = 0

#     for caractere in chave:
#         soma += ord(caractere)

#     return soma % tamanho


# def hash_polinomial(chave, tamanho):
#     base = 31
#     valor_hash = 0

#     for caractere in chave:
#         valor_hash = (valor_hash * base + ord(caractere)) % tamanho

#     return valor_hash


# # Teste
# tamanho = 10
# chave = input("Digite a chave: ")

# print("Hash por soma:", hash_soma(chave, tamanho))
# print("Hash polinomial:", hash_polinomial(chave, tamanho))