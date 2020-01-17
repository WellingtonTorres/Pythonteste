galera = list()
dado = list() #temporario
totmaior_ = totmenor_ = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade!')
        totmaior_ += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor_ += 1
print(f'Temos {totmaior_} maiores e {totmenor_} menores de idade.')
