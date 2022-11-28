import math

def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return print('A equação de 2° grau não possui raízes reais!')
    else:
        x1_numerador = (-b + math.sqrt(delta))
        x2_numerador = (-b - math.sqrt(delta))
        x_denominador = 2 * a
        x1 = x1_numerador / x_denominador
        x2 = x2_numerador / x_denominador
        return print('S = {', x1, ';', x2, '}')

a = input('Insira o valor de "a": ')
b = input('Insira o valor de "b": ')
c = input('Insira o valor de "c": ')

try:
    print(' ')
    print('Valor de "a":', a)
    print('Valor de "b":', b)
    print('Valor de "c":', c)
    a_float = float(a)
    b_float = float(b)
    c_float = float(c)
    bhaskara(a_float, b_float, c_float)
except:
    print(' ')
    print('Isso não é um número')
