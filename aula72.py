def multi(*args):
    total = 1
    for numero in args:
      total *= numero   
    return total

multiplica_1 = multi(2, 5)
print(multiplica_1)

multiplica_2 = multi(4, 7, 8)
print(multiplica_2)



def imp_ou_par():
    numeros = input('Digite seu numero:')
    numeros % 2 == 0

      
      
imp_ou_par(11)


print(4)