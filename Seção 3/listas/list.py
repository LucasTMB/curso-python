"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

string = 'ABCDE'
lista = [123, True, 'Luiz Otavio', 1.2, []]
print(bool([])) # se a lista estiver vazia, vai ser false
print(lista, type(lista))
print(lista[2], type(lista[2]))
lista[2] = 'Lucas Teixeira'
print(lista)
