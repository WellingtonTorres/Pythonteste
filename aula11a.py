print('Hello World!')
print('\033[4;30;45mHello World!')
print('\033[4;30;45mHello World!\033[m')
print('\033[7;30;47mHello World!\033[m')
print('\033[7;30mHello World!\033[m')
print('Os valores são \033[7;30m3\033[m e 5!')
print('Entre \033[7;30m20\033[m e \033[7;30m25\033[m eu prefiro \033[7;32m22\033[m (?)')
name = 'Wellington'
print('Hello! Nice to meet you, {}{}{}'.format('\033[4;34m', name, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'
        }
print('Hello! Nice to meet you, {}{}{}'.format(cores['azul'], name, cores['limpa']))
