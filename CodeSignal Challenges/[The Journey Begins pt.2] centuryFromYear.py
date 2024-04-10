"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
"""


def solution(year):
    if year % 100 == 0:
        century = year // 100
    else:
        century = year // 100 + 1
    return century


if __name__ == '__main__':
    print(solution(1905))

"""
O operador // em Python é o operador de divisão inteira. Ele retorna o quociente da divisão entre dois números, descartando a parte fracionária. Em outras palavras, ele retorna o resultado da divisão, mas arredondado para baixo para o número inteiro mais próximo.

Por exemplo:

python
Copy code
result = 10 // 3
print(result)
Neste caso, result será igual a 3, porque 10 dividido por 3 é 3 com um resto de 1, e o operador // retorna apenas a parte inteira, descartando a fração.
"""