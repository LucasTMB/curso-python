"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = False
num = 0
while condicao == False:
    print(f'Número: {num}')
    escolha = input('Você quer continuar somando? [S - Sim / N - Não]: ')

    if escolha == 'S':
        num = num + 1
    else:
        print('Fim do programa')
        print(f'Valor final: {num}')
        condicao = True



