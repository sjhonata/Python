import re
import sys

entrada_cpf = input(f'Digite seu CPF: ')
cpf_enviado = re.sub(r'[^0-9]', '', entrada_cpf)

caractere_repetido = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
if caractere_repetido:
    print(f'Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10

somaMultiplicador_1 = 0

for digito_1 in nove_digitos:
    somaMultiplicador_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (somaMultiplicador_1 * 10) % 11
primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

dez_digitos = cpf_enviado[:9] + f'{primeiro_digito}'
contador_regressivo_2 = 11

somaMultiplicador_2 = 0
for digito_2 in dez_digitos:
    somaMultiplicador_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (somaMultiplicador_2 * 10) % 11
segundo_digito = 0 if segundo_digito > 9 else segundo_digito

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print(f'CPF inválido')
