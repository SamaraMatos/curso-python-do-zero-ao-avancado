def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'prdouto 1', 'preco': 22.32},
    {'nome': 'prdouto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'prdouto 4', 'preco': 69.90},
]




novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)


novos_produtos = [
    p for p in produtos
    if p['preco'] > 100
]

print_iter(produtos)
print_iter(novos_produtos)