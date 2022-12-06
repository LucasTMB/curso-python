"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try:
    print('Valor digitado: ', num)
    num_int = int(num)
    resto = num_int % 2
    if resto == 0:
        print(f'O número {num_int} é par.')
    else:
        print(f'O número {num_int} é ímpar.')
except:
    print('Isso não é um número inteiro!')  