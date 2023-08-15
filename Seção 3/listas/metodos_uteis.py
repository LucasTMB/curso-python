'''
append - adiciona um item no final
insert - adiciona um item no indice escolhido
pop - remove do final ou do índice escolhido
del - apaga um indice
clear - limpa a lista
extende - estende a lista
+ - concatena a lista 
'''

lista = [10, 20, 30, 40]
lista.append('Lucas')
nome = lista.pop()
lista.append(1233)
del lista[-1] #eliminando o último item
# lista.clear() -- limpa a lista
lista.insert(0, 5) #(indice, valor)
print(lista)

lista2 = [100, 200, 300]
lista3 = lista + lista2
print(lista3)

lista.extend(lista2) # esse método faz a ação, mas n retorna o valor de volta
print(lista)