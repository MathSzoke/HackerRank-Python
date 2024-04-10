"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
"""


def solution(inputString):
    if inputString[:: -1] == inputString:
        return True
    else:
        return False


if __name__ == '__main__':
    print(solution("aabaa"))


"""
O seguinte trecho de código:

inputString[:: -1] == inputString

faz o seguinte:

[:: -1] reverte a string, ou seja, se o valor da variavel 'inputString' for 'Batata', ao utilizar o [:: -1], irá reverter a string tornando-o em "atataB".
O if verifica se a string passada no parametro quando é revertida é igual a string passada no parametro sem ser revertida.

Se for igual mesmo revertendo a String, é um Palíndromo, caso contrário, não é.
"""