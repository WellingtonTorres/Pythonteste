lanche = ('hamburguer', 'pizza', 'pudim', 'suco')
#Tuplas são imutaveis
for c in lanche:
    print(f'Tem: {c}')
for c in range(0, len(lanche)):
    print(lanche[c])
    for pos, comida in enumerate(lanche):
        print(f'Comer: {comida} na posição: {pos}')
print(sorted(lanche))
