frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(', ') # separa a stringa com base no valor selecionado

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) # corta os espaços em branco no começo e fim da frase
    #rstrip: corta o espaço a direita
    #lstrip: corta espaço apenas na esquerda

print(lista_frases)

frases_unidas = '-'.join('abc') #a-b-c
print(frases_unidas)