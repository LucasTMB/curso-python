valor_com = 1
valor_financ = 35
classif_servico = 'DDRD'

if valor_com == 1 or valor_com == 10:
    if valor_financ == 35 or valor_financ == 36 or valor_financ == 38 or valor_financ == 40 or valor_financ == 42:
        indicador_situacao = 2
    else:
        indicador_situacao = 1

    if (valor_com == 1 and (valor_financ == 36 or valor_financ == 38)) or (classif_servico == 'LIRT' and indicador_situacao == 1):
        print('SITUACAO A')
    else:
        if (classif_servico == 'LTCA' or classif_servico == 'LTRA' or classif_servico == 'TUPC' or classif_servico == 'TUPM' or classif_servico == 'DDRD') and (valor_com == 15 or valor_com == 16 or valor_com == 17):
            print('SITUACAO B')
        else:
            print('SITUACAO C')
else:
    if valor_financ == 35 or valor_financ == 36 or valor_financ == 38 or valor_financ == 40 or valor_financ == 42:
        print('SITUACAO D')
    else:
        if valor_financ != 36 and valor_financ != 38 and classif_servico == 'LIRT':
            print('SITUACAO E')
        else:
            print('SITUACAO F')
