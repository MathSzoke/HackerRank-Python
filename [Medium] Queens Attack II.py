#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

# - int n: o número de linhas e colunas no tabuleiro
# - int k: o número de obstaculos no tabuleiro
# - int r_q: o número da linha da posição atual da rainha
# - int c_q: o número da coluna da posição atual da rainha
# - int obstacles[k][2]: cada elemento em um array de 2 inteiros, significa a linha e coluna de um obstáculo

# Returns
# - int: o número de quadrados que a rainha pode atacar/mover
def queensAttack(n, k, r_q, c_q, obstacles):
    # Converte a lista de obstáculos em um conjunto para verificação rápida de obstáculos
    obstacles = {(r, c) for r, c in obstacles}

    # Inicializa o contador de movimentos possíveis para a rainha
    count = 0

    # Define as direções possíveis para a rainha se mover
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Para cada direção, verifica se a rainha pode se mover naquela direção
    for dr, dc in directions:
        # Calcula a próxima posição na direção atual
        r, c = r_q + dr, c_q + dc
        # Enquanto a próxima posição estiver dentro do tabuleiro e não for um obstáculo
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obstacles:
            # Incrementa o contador de movimentos possíveis
            count += 1
            # Calcula a próxima posição na mesma direção
            r, c = r + dr, c + dc

    # Retorna o total de movimentos possíveis
    return count

if __name__ == '__main__':
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [[5, 5], [4, 2], [2, 3]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
