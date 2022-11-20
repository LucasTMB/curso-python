nome = input("Insira o seu nome: ")
altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))
imc = peso / altura ** 2
tipo_imc = ...

if imc < 16:
    tipo_imc = "magreza grave"
elif imc >= 16 and imc < 17:
    tipo_imc = "magreza moderada"
elif imc >= 17 and imc < 18.5:
    tipo_imc = "magreza leve"
elif imc >= 18.5 and imc < 25:
    tipo_imc = "um corpo saudável"
elif imc >= 25 and imc < 30:
    tipo_imc = "sobrepeso"
elif imc >= 30 and imc < 35:
    tipo_imc = "obesidade grau I"
elif imc >= 35 and imc < 40:
    tipo_imc = "obesidade grau II"
else:
    tipo_imc = "obesidade mórbida" 

linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso}kg e tem um IMC de {imc:.1f}, possuindo {tipo_imc}'

print(linha_1)