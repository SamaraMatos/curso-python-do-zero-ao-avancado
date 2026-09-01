# list comprehension

#print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# #print(lista)

# lista =[numero for numero in range(10)]
# print(lista)

# lista =[
#     numero * 2
#         for numero in range(10)
# ]
# print(lista)

import pprint

def p(v):
    pprint.pprint(v)
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 30, },
    {'nome': 'p3', 'preço': 10, },

]
novos_produtos = [
    {**produto, 'preço': produto ['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]
#print(*novos_produtos, sep='\n')
 
# p(novos_produtos)
lista = [n for n in range(10)]
print(lista)
