def imprimir_matriz(matriz):
    for linha in matriz:
        print(" | ".join(map(str, linha)))
        print("-" * 9)

def fazer_jogada(matriz, matriz_jogador):
    while True:
        imprimir_matriz(matriz)

        escolha_linha = int(input("Digite o número da linha (0, 1, ou 2): "))
        escolha_coluna = int(input("Digite o número da coluna (0, 1, ou 2): "))

        if 0 <= escolha_linha < 3 and 0 <= escolha_coluna < 3 and matriz_jogador[escolha_linha][escolha_coluna] == "_":
            matriz[escolha_linha][escolha_coluna] = "X"
            matriz_jogador[escolha_linha][escolha_coluna] = "X"
            break
        else:
            print("Posição inválida ou já escolhida. Escolha uma posição válida.")

    print("Jogada do jogador realizada com sucesso!")
    
    if verificar_vitoria(matriz, "X"):
        imprimir_matriz(matriz)
        print("Parabéns! Você ganhou!")
        exit() 

    return imprimir_matriz(matriz)

def jogada_pc(matriz, matriz_jogador):
    import random

    print("Agora seu belo computador irá realizar a jogada dele")

    while True:
        escolha_linha = random.randint(0, 2)
        escolha_coluna = random.randint(0, 2)

        if matriz_jogador[escolha_linha][escolha_coluna] == "_":
            matriz[escolha_linha][escolha_coluna] = "O"
            matriz_jogador[escolha_linha][escolha_coluna] = "O"
            break
        
    if verificar_vitoria(matriz, "O"):
        print("Seu computador venceu! Seu burro incompetente.")
        exit()

    return imprimir_matriz(matriz)

def verificar_vitoria(matriz, simbolo):
    #linhas
    for linha in matriz:
        if all(elemento == simbolo for elemento in linha):
            return True

    #colunas
    for coluna in range(3):
        if all(matriz[linha][coluna] == simbolo for linha in range(3)):
            return True

    #diagonais
    if all(matriz[i][i] == simbolo for i in range(3)) or all(matriz[i][2 - i] == simbolo for i in range(3)):
        return True

    return False

matriz = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

matriz_jogador = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

while True:
    fazer_jogada(matriz, matriz_jogador)
    jogada_pc(matriz, matriz_jogador)