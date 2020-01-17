valores_ = []

valores_.append(3)
valores_.append(9)
valores_.append(7)
for v in valores_:
    print(f'{v}', end=' ')
print('for x in FIM')
print('=-=' * 15)
for pos_, valor_ in enumerate(valores_):
    print(f'Na posição {pos_} encontrei o valor {valor_}.')
print('for c, p in ENUMARETE FIM')