def calculaDiretamente(num1_1gra, num2_1gra, num1_2gra):
    cruzamento = num2_1gra * num1_2gra
    valorX = cruzamento / num1_1gra
    return round(valorX, 2)


def calculaInversamente(num1_1gra, num2_1gra, num1_2gra):
    cruzamento = num1_1gra * num1_2gra
    valorX = cruzamento / num2_1gra
    return round(valorX, 2)

resultado = None

print('Olá! Essa é uma calculadora para regra de três simples.\n')

print('INSTRUÇÕES!\n')

print('1 - Identificar as grandezas e construção da tabela.')
print('2 - Analisar se as grandezas são diretamente ou inversamente proporcionais. Se for diretamente, basta realizar apenas a multiplicação cruzada. Se for inversamente, é necessário inverter o numerador e denominador de uma das frações.')
print('3 - Aplicar o método de resolução correto para cada um dos casos, e, por fim, resolver a equação.\n')

print('VAMOS COMEÇAR!\n')

condicao1 = False
while condicao1 == False:
    print('ATENÇÃO! Por gentileza, insira apenas números inteiros.\n')

    num1_1grandeza = input('Digite o primeiro valor da primeira grandeza: ')
    num2_1grandeza = input('Digite o segundo valor da primeira grandeza: ')
    num1_2grandeza = input('Digite o primeiro valor da segunda grandeza: ')

    try:
        print(' ')
        print(f'Primeiro valor da primeira grandeza: {num1_1grandeza}')
        print(f'Segundo valor da primeira grandeza: {num2_1grandeza}')
        print(f'Primeiro valor da segunda grandeza: {num1_2grandeza}')
        print(f'Segundo valor da segunda grandeza: x')
        num1_1grandeza_int = int(num1_1grandeza)
        num2_1grandeza_int = int(num2_1grandeza)
        num1_2grandeza_int = int(num1_2grandeza)
        condicao1 = True;
    except:
        print(' ')
        print('[ERRO!] Isso não é um número! Insira um valor inteiro válido.\n')

condicao2 = False 
while condicao2 == False:
    print('Sua regra de três é diretamente ou inversamente proporcional?\n')
    diretamente_ou_inversamente = input('Diretamente [D ou d] / Inversamente [I ou i]: ')
    diretamente = diretamente_ou_inversamente == 'D' or diretamente_ou_inversamente == 'd'
    inversamente = diretamente_ou_inversamente == 'I' or diretamente_ou_inversamente == 'i'

    if diretamente:
        print('Foi escolhido o diretamente!')
        resultado = calculaDiretamente(num1_1grandeza_int, num2_1grandeza_int, num1_2grandeza_int)
        condicao2 = True
    elif inversamente:
        print('Foi escolhido o inversamente!')
        resultado = calculaInversamente(num1_1grandeza_int, num2_1grandeza_int, num1_2grandeza_int)
        condicao2 = True
    else:
        print('\n[ERRO!] Escolha uma opção válida!\n')

print(' ')
print(f'x = {resultado}')