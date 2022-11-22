nome = 'Lucas'

print(nome[3])
print('u' in nome)

encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está inserido em {nome}')
else:
    print(f'{encontrar} não está inserido em {nome}')