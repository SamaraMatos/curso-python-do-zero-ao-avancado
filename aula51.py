'''
Introdução ao desempacotamento
'''
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2, nome1,)

nome1, *resto = ['Maria', 'Helena', 'Luiz'] # ou se usa o *_
print(nome1)