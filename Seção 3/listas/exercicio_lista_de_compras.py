import os

condicao = False
lista = []

while condicao != True:
    print('Escolha uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    if opcao == 'i' or opcao == 'I':
        
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a' or opcao == 'A':
        indice = input('Escolha o indice para apagar: ')
        
        try:
            indice_int = int(indice)
            del lista[indice_int]
            print('Item apagado.')
        except ValueError:
            print('Por favor digite números inteiros.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
        
    elif opcao == 'l' or opcao == 'L':
        
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        for indice, item in enumerate(lista):
            print(indice, item)
    elif opcao == 's' or opcao == 'S':
        print('Programa encerrado.')
        condicao = True
    else:
        print('Escolha uma opção válida.')