from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'Joao', 'Joana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]

# print_iter(combinations(pessoas, 2)) # sep='\n' quebra em linhas # combinations combina o itens da lista de pessoas em 2, o *list desempacota 
# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))
