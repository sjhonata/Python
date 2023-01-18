palavra_secreta = 'melancia'
letra_acertada = ''
cont = 0 

while True:
    
    letra_digitada = input(f'Digite uma letra: ')
    cont += 1

    if len(letra_digitada) > 1:
        print(f'Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print()
        print(f'Você acertou! Parabéns!')
        print(f'A palavra certa era {palavra_secreta}')
        print(f'Tentativas: {cont} vezes')
        break

 