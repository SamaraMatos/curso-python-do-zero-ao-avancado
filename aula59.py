string = 'ABCD '
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

a, b, *_, u = lista
print(a, b,)
print(lista)
print(*lista)
print(*lista, sep='\n')