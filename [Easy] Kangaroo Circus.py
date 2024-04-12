#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1 kangaroo1 started in this position
#  2. INTEGER v1 kangaroo1 jumps in this distance
#  3. INTEGER x2 kangaroo2 started in this position
#  4. INTEGER v2 kangaroo2 jumps in this distance
#

def kangaroo(x1, v1, x2, v2):
    # Se o Canguru 1 começar adiante e pula mais rápido, eles nunca vão se encontrar
    if x1 > x2 and v1 >= v2:
        return "NO"
    # Se o Canguru 2 começar adiante e pula mais rápido, eles nunca vão se encontrar
    if x2 > x1 and v2 >= v1:
        return "NO"
    # Se suas velocidades relativas permitem eles se encontrarem na mesma posição
    if (x1 - x2) % (v2 - v1) == 0:
        return "YES"
    # Em outro caso, eles nunca vão se encontrar
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
