'''
Formatação básica de strings
s - string
d e i - int
f - float
.<número de digitos>f
x e X hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex: 0>-100,.1f
conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:,>10}')
print(f'{variavel:a<10}')
print(f'{variavel:b^10}')
print(f'{1000.65431351515:.1f}')
print('o hexadecimal de 1500 é {1500:08x}') 
print(f'{variavel!r}')