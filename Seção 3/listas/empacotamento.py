nomes = ['Maria', 'Lucas', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

carro1, *resto = ['Ferrari', 'Audi', 'BMW']
print(carro1, resto)

#se eu não querer usar o resto
ferramenta1, *_ = ['Marreta', 'Martelo'] # ainda salva no _, mas é uma convenção para avisar a outros programadores pra n usar essa variavel
print(ferramenta1)