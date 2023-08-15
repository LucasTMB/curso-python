salas = [
    #0         1
    ['Maria', 'Helena', ], # 0
    #0
    ['Elaine', ], # 1
    #0       1        2         3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20)] # 2
]

print(salas[2][3][2]) # 20

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala: 
        print(aluno)