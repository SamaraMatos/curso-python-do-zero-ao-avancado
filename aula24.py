#operadores in e not in 
# strings são iteraveis
# 0 1 2 3 4 5
# S A M A R A
# -6-5-4-3-2-1

nome = 'SAMARA'
print(nome[2])
print(nome[3])

print ('o' in nome)
print ('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
