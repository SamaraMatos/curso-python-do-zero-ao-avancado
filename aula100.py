import copy
 
produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def ver_produtos():
    for p in produtos:
        print(f"{p['nome']:<10} -R$ {p['preco']:<6.2f}")
    print('Produtos e valores acima.\n')


def aumento_valor():
    novos_produtos = copy.deepcopy(produtos)
    aumento = 0.10
    for p in novos_produtos:
      p["preco"] *= (1 + aumento)
      print(f"{p['nome']:<10} -R$ {p['preco']:<6.2f}")    
    print('Esse produto estão com aumento de 10%\n')
    

def produtos_ordenados():
    produtos_ordenados = copy.deepcopy(produtos)
    produtos_ordenados.sort(key=lambda n: n["nome"], reverse=True)
    for p in produtos_ordenados:
        print(f"{p['nome']:<10} -R$ {p['preco']:<6.2f}")
    print('Produtos ordenados do maior ao menor.\n')


def produto_ordenador_por_preco():
    produto_ordenador_por_preco = copy.deepcopy(produtos)
    produto_ordenador_por_preco.sort(key=lambda p: p["preco"])
    for p in produto_ordenador_por_preco:
        print(f"{p['nome']:<10} -R$ {p['preco']:<6.2f}")
    print('Produtos ordenados pelo preço menor ao maior.\n')

while True:
    print('(1) Produtos e Preços')
    print('(2) Produtos com aumento de preço')
    print('(3) Produtos em ordem decrescente')
    print('(4)Produto em ordem pelo preço')
    print('Digite 0 para sair\n')

    opcao = input('Digite a opção desejada:\n')

    if opcao == '1':
        ver_produtos()

    elif opcao == '2':
        aumento_valor()

    elif opcao == '3':
        produtos_ordenados()

    elif opcao == '4':
        produto_ordenador_por_preco()

    elif opcao == '0':
        print('Saindo do programa, até logo!')
        break

    else: 
        print('Opcão inválida. Tente novamente.\n')
        
