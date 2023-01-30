import random


nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10

somaMultiplicador_1 = 0

for digito_1 in nove_digitos:
    somaMultiplicador_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (somaMultiplicador_1 * 10) % 11
primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11

somaMultiplicador_2 = 0
for digito_2 in dez_digitos:
    somaMultiplicador_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (somaMultiplicador_2 * 10) % 11
segundo_digito = 0 if segundo_digito > 9 else segundo_digito

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(f'CPF gerado: {cpf_gerado}')
