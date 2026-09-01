'''
for in com listas
'''

lista = ['Maria', 'Helena', 'Luiz']

for indice, lista in enumerate(lista):
    nome = lista
    print(indice, nome)

#ooooouuu

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Samara')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
