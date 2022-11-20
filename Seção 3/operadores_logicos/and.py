login = 'abc@tuamaeaquelaursa.com'
login_digitado = input('Email: ')
senha = 'abc123'
senha_digitada = input('Senha: ')

if login_digitado == login and senha_digitada == senha:
    print('Entrada confirmada!')
else:
    print('Dados inválidos')