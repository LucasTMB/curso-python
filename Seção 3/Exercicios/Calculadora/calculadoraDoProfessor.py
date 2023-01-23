while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if len(operador) > 1:
        print('Operador inválido')
        continue

    print('Realizando sua conta. Resultado abaixo: ')

    if operador == '+':
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
    else:
        print('Nunca deveria ter chegado aqui')

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    
    if sair is True:
        break