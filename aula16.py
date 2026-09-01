#if / elif      / else
#se/ se não se    / se não

entrada = input('Você quer entrar o sair?')

if entrada == 'entrar':
    print('você entrou no sistema')
    print('dentro do bloco if')
elif entrada == 'sair':
    print('você saiu do sistema')
    print('dentro do bloco elif')
else: 
    print('você não digitou nem entrar e nem sair')
    print('dentro do bloco else')


    print('fora do bloco')