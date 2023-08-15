lista = ['Ferrari', 'Audi', 'BMW']
#lista_enumerada = enumerate(lista)

for item in enumerate(lista): # dessa forma posso fazer quantos interator eu quiser
    print(item)
    
for indice, carro in enumerate(lista): 
    print(indice, carro)