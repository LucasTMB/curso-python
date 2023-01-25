frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

frase_lower = frase.lower()

#print(frase.lower().count('python'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase_lower):
    letra_atual = frase_lower[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase_lower.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra q apareceu mais vezes foi "{letra_apareceu_mais_vezes}", aparecendo {qtd_apareceu_mais_vezes} vezes')