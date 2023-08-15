import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo = 10
    resultado_1 = 0

    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo
        contador_regressivo -= 1 

    primeiro_digito = (resultado_1 * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    cpf_com_digito = nove_digitos + str(primeiro_digito)

    contador_regressivo = 11
    resultado_2 = 0

    for digito in cpf_com_digito:
        resultado_2 += int(digito) * contador_regressivo
        contador_regressivo -= 1
        
    segundo_digito = (resultado_2 * 10) % 11

    if segundo_digito > 9:
        segundo_digito = 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado_pelo_calculo)