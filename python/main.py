from helpers import gera_grid, renderiza_grid, desenha_grid, atualiza_matrix
import os
from time import sleep


def main():
    grid = gera_grid(20, 20)
    renderiza_grid(grid)
    try:
        while True:
            desenha_grid(grid)
            grid = atualiza_matrix(grid)
            sleep(0.3)
            os.system('clear')
    except KeyboardInterrupt:
        print('cabou')


main()
