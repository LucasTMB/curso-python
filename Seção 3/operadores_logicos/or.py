entrada = input("[E]ntrar [S]air: ")

if entrada == 'E' or entrada == 'e':
    print("Entrou")
elif entrada == 'S' or entrada == 's':
    print("Saiu")
else:
    print("Opção inválida!")

senha = input('Senha: ') or 'Sem senha'
print(senha)