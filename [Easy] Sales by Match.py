#!/bin/python3
import collections
import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar


# O operador // em Python é o operador de divisão inteira, que retorna a parte inteira do resultado da divisão.
# Por exemplo, 5 // 2 resultará em 2, pois a parte inteira de 5 dividido por 2 é 2, e não 2.5.

def sockMerchant(n, ar):  # Define a função sockMerchant que recebe dois argumentos: n (número total de elementos na lista) e ar (a lista de elementos).
    pairs = 0  # Inicializa a variável pairs que será usada para contar o número de pares de elementos.
    counter = Counter(ar)  # Usa a função Counter do módulo collections para contar a frequência de cada elemento na lista ar e cria um dicionário com essas contagens.
    repeats = [elemento for elemento, frequencia in counter.items() if frequencia >= 2]  # Cria uma lista com os elementos que se repetem ao menos duas vezes.
    for item in repeats:  # Itera sobre os elementos repetidos.
        if counter[item] >= 2:  # Verifica se o elemento se repete ao menos duas vezes.
            pairs += counter[item] // 2  # Adiciona ao número de pares a quantidade de pares que o elemento forma.

    return pairs  # Retorna o número total de pares encontrados na lista ar.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
