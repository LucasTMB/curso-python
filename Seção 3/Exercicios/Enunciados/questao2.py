"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex:

Bom dia 0 - 11, Boa tarde 12 - 17 e Boa noite 18 - 23
"""

hora = input('Digite o horário: ')

try:
    print('Valor digitado:', hora)
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia! São {hora_int}h da manhã.')
    elif hora_int > 11 and hora_int <= 17:
        print(f'Boa tarde! São {hora_int}h da tarde.')
    elif hora_int > 17 and hora_int < 24:
        print(f'Boa noite! São {hora_int}h da noite.')
    else: 
        print('Horário fora da faixa permitida.')
except:
    print('Isso não é um número.')