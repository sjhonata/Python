# pessoa = dict(nome='Jhonata', sobrenome='Sousa')

pessoa = {
    'nome': 'Jhonata',
    'sobrenome': 'Sousa',
    'idade': 29,
    'altura': 1.73,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])