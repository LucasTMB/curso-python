'''
Cuidado com dados mutáveis
= - copiado o valor (imutável)
= - aponta para o mesmo valor na memória (mutável)

nome = 'Lucas'
noutra_variavel = nome
nome = 'João'

print(nome)
print(noutra_variavel)
'''

lista_a = ['Lucas', 'Maria']
lista_b = lista_a # não copia a lista_a, apenas aponta para o mesmo lugar da memória

print(lista_b) # se eu alterar a lista_a, vai modificar a lista_b