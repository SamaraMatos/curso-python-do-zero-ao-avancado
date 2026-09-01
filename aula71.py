x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

#def soma(x,y):
 #   return x + y

def soma(*args):
    total = 0
    for numero in args:
        print('total', total, numero)
        total = total + numero
        print('total', total)

soma(1, 2, 3, 4, 5, 6)



def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)


outra_soma = soma(5, 78, 7)
print(outra_soma)

print(sum((5, 78, 7)))