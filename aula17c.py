#Ligação Vs Cópia da lista
a = [2, 3, 4, 7]
b = a
b[2] = 8# Aqui tentarei alterar a posição dois da lista B
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('Veja que não foi possivel aletar apenas a lista B')
print('=' * 20)
###Aqui a forma correta de criar uma cópia sem ligação a lista A
a = [2, 3, 4, 7]
b = a[:] # O segredo esta aqui, no fatiamento da lista.
b[2] = 8# Aqui tentarei alterar a posição dois da lista B
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('Observe que objetivo de alterar apenas uma lista foi concluido')
print('=' * 20)