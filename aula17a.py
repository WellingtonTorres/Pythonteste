num_ = [2, 5, 9, 1]
num_[2] = 3
num_.append(7)
num_.sort(reverse=True)
num_.insert(2, 2)
#num_.pop() #removem elimina o ultimo elemento da lista caso index não seja adiconado
if 4 in num_:
    num_.remove(4) #remove o valor que esta indexado, no caso o primeiro se houver mais de um.
else:
    print('Não há o número 4!')
print(num_)
print(f'Esta lista tem {len(num_)} elementos.')
