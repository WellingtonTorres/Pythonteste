lista_ = []
lista_.append(2)
print(lista_[-1])
lista_.insert(lista_.index(lista_[-1]) + 1, 4)
print(lista_)
print(lista_[-1])
lista_.append(3)
print(lista_)
print(lista_[-1])
#print(lista_.index(lista_[-1]))
#lista_.insert(lista_.index(lista_[-1])+1, 5)
#lista_.insert(lista_.index(lista_[-1]), 7)
#lista_.insert(lista_.index(lista_[-1]), 1)
#lista_.insert(lista_.index(lista_[-1]), 3)

'''if n > lista_[-1]:
    lista_.insert(lista_.index(lista_[-1])+1, n)
print(lista_)'''
#elif valores_ >= lista_[-1]:
#lista_.insert(lista_.index(lista_[-1]) + 1, valores_)