# import re
import sys

cpf = '723.814.990-75'
cpf_enviado = cpf.replace('-', '').replace('.', '').replace(' ', '')
"""
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    cpf
)
"""
entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf_enviado[:9]

contador_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1 

primeiro_digito = (resultado * 10) % 11

if primeiro_digito > 9:
    primeiro_digito = 0

print(f'O primeiro dígito é: {primeiro_digito}')

cpf_com_digito = nove_digitos + str(primeiro_digito)

contador_regressivo = 11
resultado = 0

for digito in cpf_com_digito:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
    
segundo_digito = (resultado * 10) % 11

if segundo_digito > 9:
    segundo_digito = 0
    
print(f'O segundo dígito é: {segundo_digito}')

cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado == cpf_gerado_pelo_calculo:
    print(f'O CPF {cpf} é válido!')
else:
    print(f'O CPF {cpf} é inválido.')