'''
eumerate - enumera iteráveis (índices)
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Samara')

lista_enumerada = list(enumerate(lista, start=2)) # start serve para comecar apartir de tal indice

for item in enumerate(lista):
    print(item)
    
for indice, nome in enumerate(lista):
    print(indice, nome)
    