import random


def gera_grid(colunas, linhas):
    return [[0] * colunas for r in range(linhas)]


def renderiza_grid(grid):
    for linhas in range(1, len(grid) - 1):
        for colunas in range(1, len(grid[0]) - 1):
            grid[linhas][colunas] = random.randint(0, 1)


def mapeia_vizinhos(matrix, x, y):
    ref = 0
    if matrix[x][y] == 0:
        ref = ref
    else:
        ref = -1
    for _x in range(-1, 2):
        for _y in range(-1, 2):
            vizinhosx = x + _x
            vizinhosy = y + _y
            if (vizinhosx >= 0 and vizinhosy >= 0) and (vizinhosx < len(matrix) and vizinhosy < len(matrix[0])):
                ref += matrix[vizinhosx][vizinhosy]
    return ref


def desenha_grid(grid):
    for linhas in grid:
        for colunas in linhas:
            print('.' if colunas == 0 else '*', end='')
        print()


def atualiza_matrix(matrix):
    nova_matrix = gera_grid(len(matrix), len(matrix[0]))
    for linhas in range(len(matrix)):
        for colunas in range(len(matrix[0])):
            vizinho = mapeia_vizinhos(matrix, linhas, colunas)
            if matrix[linhas][colunas] == 0 and vizinho == 3:
                nova_matrix[linhas][colunas] = 1
            if matrix[linhas][colunas] == 1:
                if vizinho < 2:
                    nova_matrix[linhas][colunas] = 0
                elif vizinho > 3:
                    nova_matrix[linhas][colunas] = 0
                else:
                    nova_matrix[linhas][colunas] = 1
    return nova_matrix
