'''
teste = list()
teste.append('Gustavo')
teste.append(60)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)
'''
galera = [['Joao', 19], ['Ana', 33], ['Vicente', 27], ['Maria Eduarda', 15]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[:2])
print('-=-=-=-=-=-=Laço Repetição=-=-=-=-=')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
