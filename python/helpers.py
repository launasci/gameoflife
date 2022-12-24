import random


def gera_grid(colunas, linhas):
    # inicia o grid do jogo fazendo um for pelas linhas e mutiplicando as colunas
    return [[0] * colunas for r in range(linhas)]


def renderiza_grid(grid):
    # renderiza o grid fazendo um for pelas linhas, depois pelas colunas e gerando uma matriz aleatoria com o randint()
    for linhas in range(1, len(grid) - 1):
        for colunas in range(1, len(grid[0]) - 1):
            grid[linhas][colunas] = random.randint(0, 1)


def mapeia_vizinhos(matriz, x, y):
    # mapeias os vizinhos das celulas de referencia, não levando em consideração a propria celula para contar os vizinhos
    ref = 0
    if matriz[x][y] == 0:
        ref = ref
    else:
        ref = -1
# faz um for primeiro pelo eixo x e depois pelo eixo y pegando como referência da matriz, a partir da celula, -1, 0, 1, 2
# atribui os valores aos vizinhos por eixo e depois verifica as bordas da matriz, isso é o seu tamanho
# salva na ref o valor de vizinhos
    for _x in range(-1, 2):
        for _y in range(-1, 2):
            vizinhosx = x + _x
            vizinhosy = y + _y
            if (vizinhosx >= 0 and vizinhosy >= 0) and (vizinhosx < len(matriz) and vizinhosy < len(matriz[0])):
                ref += matriz[vizinhosx][vizinhosy]
    return ref


def desenha_grid(grid):
    # desenha o grid de acordo com o status da celular, se 0 igual a morta, se 1 igual a viva
    for linhas in grid:
        for colunas in linhas:
            print('\U0001F480' if colunas == 0 else '\U0001F92A', end='')
        print()


def atualiza_matriz(matriz):
    # atualiza a matriz, primeiro fazendo um for pelas linhas que usa como base o len da matriz e depois pelas colunas
    # chama a função mapeia vizinhos, dentro do loop aninhado passando como parametros a matriz, linhas, colunas
    # por fim aplica as regras dos jogo de acordo com a quantidade de vizinhos
    nova_matriz = gera_grid(len(matriz), len(matriz[0]))
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[0])):
            vizinho = mapeia_vizinhos(matriz, linhas, colunas)
            if matriz[linhas][colunas] == 0 and vizinho == 3:
                nova_matriz[linhas][colunas] = 1
            if matriz[linhas][colunas] == 1:
                if vizinho < 2:
                    nova_matriz[linhas][colunas] = 0
                elif vizinho > 3:
                    nova_matriz[linhas][colunas] = 0
                else:
                    nova_matriz[linhas][colunas] = 1
    return nova_matriz
