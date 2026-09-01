perguntas = [
    {
        'pergunta': 'quanto é 2+2?',
        'opções': ['1', '2', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'quanto é 5*5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'pergunta': 'quantos é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5',
    },
]



# def pergunta1():
#     print(perguntas[0]['pergunta'])
#     print(perguntas[0]['opções'])
#     opcao = input('Digite umas das opçoes acima: ')
#     if opcao == perguntas[0]['resposta']:
#         print('Parabéns, voce acertou')
#     else:
#         print('Você errou')

# def perguntas2():
#     print(perguntas[1]['pergunta'])
#     print(perguntas[1]['opções'])
#     opcao = input('Digite umas das opçoes acima: ')
#     if opcao == perguntas[1]['resposta']:
#         print('Parabéns, voce acertou')
#     else:
#         print('Você errou')

# def perguntas3():
#     print(perguntas[2]['pergunta'])
#     print(perguntas[2]['opções'])
#     opcao = input('Digite umas das opçoes acima: ')
#     if opcao == perguntas[2]['resposta']:
#         print('Parabéns, voce acertou')
#     else:
#         print('Você errou')

# while True:
#     print('responda as questoes a baixo:')
#     pergunta1()
#     perguntas2()
#     perguntas3()
#     break
        
    
  ######################################  

for pergunta in perguntas:
    print(pergunta['pergunta'])
    print()

    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
         if opcoes[escolha_int] == pergunta['resposta']:
            acertou = True
    if acertou:
       print('Você acertou')
    else:
       print('Você errou')


print('Você acertou', qtd_opcoes)
print('de', len(pergunta), 'perguntas')

