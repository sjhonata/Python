"""
O usuario deve ter a possibilidade de inserir, apagar e listar valores de sua lista.
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

import os

lista = []

while True:
    print(f'Selecione uma opção')
    opcao = input(f'[i]nserir  [a]pagar  [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input(f'Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(f'Qual indice deseja apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print(f'Por favor digite um número inteiro.')
        except IndexError:
            print(f'O índice digitado não existe na lista.')
        except Exception:
            print(f'Erro desconhecido.')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print(f'Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print(f'Por favor, escolha i, a ou l.')