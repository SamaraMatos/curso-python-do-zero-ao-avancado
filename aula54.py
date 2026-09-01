
lista = []

while True:
    print('Adicionar itens na lista, selecione "1"')
    print('lista itens da lista, selecione "2"')
    print('Deletar itens da lista, selecione "3"')
    
    opcao = input('Selecione a sua opção:')

    if opcao == '1':
        
        add_lista = input('Digite o itém que você deseja adicionar na lista:')
        lista.append(add_lista)
        print('Itém cadastrado com sucesso')
    
    elif opcao == '2':
        if len(lista)== 0:
            print('Não a nada em sua lista')
        
        for i, valor in enumerate(lista):
         print(i, valor)

    elif opcao == '3':
        item_selc = input('Escolha um itém para apagar')
        item = int(item_selc)
        del lista[item]

    else:
        print('Opção inválida')

            

    
    





        
