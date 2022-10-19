"""
Iniciar com letra, pode conter números, separar _, letras minusculas
"""
nome = 'Lucas'
idade = 32
altura = 1.70
peso = 70
e_maior = idade > 18
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu IMC é de', imc)