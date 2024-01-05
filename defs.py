
def iniciar_jogo():
    matriz = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    
    for linha in matriz:
        print(linha)
        
def fazer_jogada():
    if escolha_linha and escolha_coluna > 0:
        for escolha_linha in range (len(matriz)):
                for escolha_coluna in range (len(matriz)):
                    print(matriz[escolha_linha, escolha_coluna])
                    

iniciar_jogo()

escolha_linha = int(input("digite o número da linha"))
escolha_coluna = int(input("digite o número da coluna"))

fazer_jogada()