altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

imc = peso / (altura * altura)
print("IMC:", imc)

if imc < 16:
    print("Você possui magreza grave")
elif imc >= 16 and imc < 17:
    print("Você possui magreza moderada")
elif imc >= 17 and imc < 18.5:
    print("Você possui magreza leve")
elif imc >= 18.5 and imc < 25:
    print("Você está saudável")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso")
elif imc >= 30 and imc < 35:
    print("Você possui obesidade grau I")
elif imc >= 35 and imc < 40:
    print("Você possui obesidade grau II")
else:
    print("Você possui obesidade mórbida") 