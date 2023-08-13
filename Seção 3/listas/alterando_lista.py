lista = [10, 20, 30, 40]

# adicionando itens
lista.append(50)
lista.pop() # removendo o último elemento e retorna esse elemento
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)