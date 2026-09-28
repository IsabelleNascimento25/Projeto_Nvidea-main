# chaves = [13, 25, 31, 44, 57, 55, 55, 33]
# tamanho = 10
# colisoes = {}
# indices

# for chave in chaves:
#     indice = (chave % tamanho)
#     print(f"Chave: {chave} Indice: {indice}")

# colisoes

# for chave in chaves:
#         indice = (chave % tamanho)
#         # define a estrutura do dicionario
#         colisoes.setdefault(indice, []).append(chave)   

# print("Buscando Colisoes")
# for indice, colisao in colisoes.items():
#        if len(colisao) > 1:
#              print(f"Colisão no indice {indice}: {colisao}")



chaves = ["ANA", "NAA", "CARLOS", "SACROL", "MARIA", "PEDRO"]
tamanho = 7

def funcao_hash_soma(chave, tamanho):
        soma = 0
        for caractere in chave:
            soma += ord(caractere)
        return soma % tamanho


def funcao_hash_polinomial(chave, tamanho):
        valor_hash = 0
        base = 31
        for caractere in chave:
            valor_hash = valor_hash * base + ord(caractere)
            print (valor_hash)
        return valor_hash % tamanho
# Calcule os índices gerados pelas duas funções
# Conte quantas colisões ocorreram em cada uma

###############################################################################################################################

for chave in chaves:
    indice_soma = funcao_hash_soma(chave, tamanho)
    indice_polinomial = funcao_hash_polinomial(chave, tamanho)

    print(
        f"{chave}: Soma = {indice_soma} | "
        f"Polinomial = {indice_polinomial}"
    )