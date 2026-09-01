# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort()
# print(lista)

lista = [
    {'nome': 'Samara', 'sobrenome': 'Matos'},
    {'nome': 'Ana Julia', 'sobrenome': 'Matos Francisco'},
    {'nome': 'Rebeca', 'sobrenome': 'marques'},
    {'nome': 'cleide', 'sobrenome': 'Matos Francisco'},
    {'nome': 'Emerson', 'sobrenome': 'Francisco'},
    
]

# def ordena(item):
#     print(item)
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print(item)

#ouuuuuuuu
def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista,key=lambda item : item['nome'])
l2 = sorted(lista,key=lambda item : item['sobrenome'])

exibir(l1)
exibir(l2)