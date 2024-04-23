#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

"""
Objetivo:
    Verificar se é possível organizar as bolas em containers de forma que cada container contenha apenas bolas de um único tipo,
    e nenhuma bola do mesmo tipo esteja em containers diferentes.

Params example:
    container = [[1, 4], [2, 3]]
    
Returns:
    Para cada query, imprima Possible numa nova linha se David puder satisfazer as condições acima para a matriz dada.
    Caso contrário, imprima Impossible.
    
Explains:
    container_sums = [sum(row) for row in container]: Esta linha calcula a soma das bolas em cada container.
    Ela percorre cada row em container e calcula a soma das bolas nessa linha, usando a função sum().
    O resultado é uma lista container_sums onde cada elemento representa a soma das bolas em um container específico.
    
    ball_counts = [sum(row[i] for row in container) for i in range(n)]: Esta linha calcula o número de bolas de cada tipo.
    Ela percorre cada i de 0 a n-1 (onde n é o número de tipos de bolas) e calcula a soma das bolas de tipo i em todos os containers.
    Isso é feito somando row[i] para cada row em container.
    O resultado é uma lista ball_counts onde cada elemento representa o número total de bolas de um tipo específico em todos os containers.
"""
def organizingContainers(container):
    n = len(container)  # Obtém o número de containers
    container_sums = [sum(row) for row in container]  # Calcula a soma das bolas em cada container
    ball_counts = [sum(row[i] for row in container) for i in range(n)]  # Calcula o número de bolas de cada tipo

    # Verifica se é possível organizar as bolas conforme as condições dadas
    if sorted(container_sums) == sorted(ball_counts):
        return "Possible"  # Se sim, retorna "Possible"
    else:
        return "Impossible"  # Caso contrário, retorna "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
