""" Calculadora com while """

def soma(num1, num2):
    resultadoSoma = num1 + num2
    return resultadoSoma

def subtracao(num1, num2):
    resultadoSubtracao = num1 - num2
    return resultadoSubtracao

def multiplicacao(num1, num2):
    resultadoMultiplicacao = num1 * num2
    return resultadoMultiplicacao

def divisao(num1, num2):
    resultadoDivisao = num1 + num2
    return resultadoDivisao

resultado = 0

print('Bem-vindo a Calculadora While!\n')

print('Para usá-la, é necessário inserir dois números e escolher um operador entre:\n')
print('- Soma [+]')
print('- Subtração [-]')
print('- Multiplicação [*]')
print('- Divisão [/]')
print('\nDivita-se!\n')

sao_numeros = False
while sao_numeros == False:
    num1 = input('Insira o primeiro número: ')
    num2 = input('Insira o segundo número: ')

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        sao_numeros = True
    except:
        print('\nIsso não é um número!\n')

sao_operadores = False
while sao_operadores == False:
    operador = input('Selecione um operador: ')
    if operador == '+':
        resultado = soma(num1_float, num2_float)
        sao_operadores = True
    elif operador == '-':
        resultado = subtracao(num1_float, num2_float)
        sao_operadores = True
    elif operador == '*':
        resultado = multiplicacao(num1_float, num2_float)
        sao_operadores = True
    elif operador == '/':
        resultado = divisao(num1_float, num2_float)
        sao_operadores = True
    else:
        print('Insira um operador válido')

print(f'Resultado: {resultado}')
