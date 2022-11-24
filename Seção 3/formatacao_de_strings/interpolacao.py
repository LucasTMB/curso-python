"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'Lucas'
preco = 1000.5959595
variavel = '%s, o preço é de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))