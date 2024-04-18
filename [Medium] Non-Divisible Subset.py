# Esse desafio consiste em encontrar o tamanho do maior subconjunto possível de um conjunto de números inteiros distintos, no qual a soma de quaisquer dois números no subconjunto não seja divisível por um número dado k.
#
# Por exemplo, dada a lista de números [1, 7, 2, 4] e k = 3, o maior subconjunto que atende a condição é [1, 7, 4], já que a soma de quaisquer dois números nesse subconjunto não é divisível por 3.
#
# Para resolver esse problema, você pode seguir os seguintes passos:
#
# Crie um array remainders de tamanho k inicializado com zeros.
# Para cada elemento x do conjunto, incremente remainders[x % k].
# Inicialize count como o mínimo entre remainders[0] e 1 (pois apenas um número divisível por k pode ser incluído no subconjunto).
# Para i de 1 até k/2 (exceto se k for par, então vá até k/2 - 1), adicione ao count o máximo entre remainders[i] e remainders[k-i].
# Se k for par, adicione 1 a count caso remainders[k/2] seja maior que zero (pois só pode haver um número que é k/2 no subconjunto).
# Retorne count.
# Essa abordagem garante que a soma de quaisquer dois números no subconjunto não seja divisível por k, pois para qualquer par de números (x, y) onde x % k = a e y % k = b, a + b não será divisível por k.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Passo 1: Inicializa a array com o valor 0 e com o tamanho do valor de k
    remainders = [0] * k

    # Passo 2: Incrementar os valores do array remainders
    for x in s:
        remainders[x % k] += 1

    # Passo 3: Inicializar count
    count = min(remainders[0], 1)  # Apenas um número divisível por k pode estar no subconjunto

    # Passo 4: Adicionar ao count o máximo entre remainders[i] e remainders[k-i]
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(remainders[i], remainders[k - i])

    # Passo 5: Para k par, adicionar 1 a count se remainders[k/2] for maior que zero
    if k % 2 == 0:
        count += min(remainders[k // 2], 1)

    return count

if __name__ == '__main__':
    k = 3

    s = [1, 7, 2, 4]

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')
