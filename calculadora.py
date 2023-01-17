
while True:
    numero1 = input(f'Digite um número: ')
    numero2 = input(f'Digite outro número: ')
    operador = input(f'Digite o operador(+-/*): ')

    numerosValidos = None
    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numerosValidos = True
    except:
        numerosValidos = None

    if numerosValidos is None:
        print(f'Um ou ambos os números digitados são inválidos.')
        continue

    operadoresPermitidos = '+-/*'
    if operador not in operadoresPermitidos:
        print(f'Operador inválido')
        continue

    if len(operador) > 1:
        print(f'Digite apenas um operador: ')
        continue

    print(f'Realizando sua conta. onfira o resultado abaixo: ')
    if operador == '+':
        print(f'{numero1_float} + {numero2_float} =', numero1_float + numero2_float)
    elif operador == '-':
        print(f'{numero1_float} - {numero2_float} =', numero1_float - numero2_float)
    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} =', numero1_float / numero2_float)
    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} =', numero1_float * numero2_float)
    else:
        print(f'Não deveria chegar aqui')

    sair = input(f'Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break

