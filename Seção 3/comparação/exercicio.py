primeiroValor = input('Digite um valor: ' )
segundoValor = input('Digite outro valor: ')

if primeiroValor > segundoValor:
    print(f'{primeiroValor = } é maior que o {segundoValor = }')
elif primeiroValor < segundoValor:
    print(f'{segundoValor = } é maior que o {primeiroValor = }')
elif primeiroValor == segundoValor:
    print(f'{primeiroValor = } é igual ao {segundoValor = }')