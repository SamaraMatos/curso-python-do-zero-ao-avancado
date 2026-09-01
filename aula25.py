'''
Interpolaçõa básica  de strings
s - string
d e i - int
f - float
x e X hexadecimal (ABCDEF0123456789)

criar a variavel usar % e o usar o tipo e depois os valores
'''

nome = "Samara"
preco =  1000.95897643
variavel = '%s, o preco é R$%.2f' %(nome, preco)
print(variavel)

print('o hexadecimal de %d é %08x' % (15, 15))