dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados)
dados['sexo'] = 'M'
print(dados)
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())
for k, v in dados.items():
    print(f'O {k} é {v}')

del dados['idade']
