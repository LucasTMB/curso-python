nome = 'Lucas Teixeira'

print(nome)
print(len(nome))

contador = 0
novo_nome = ''

while contador < len(nome):
    print(nome[contador])
    novo_nome += f'*{nome[contador]}'
    contador += 1

print(novo_nome)