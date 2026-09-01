'''
split e join com list e str
split - divide uma string
join - une uma string
'''
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')

for i, frase in enumerate(lista_palavras):
 print(lista_palavras[i].strip())

print(lista_palavras)


frase_unidas = '-'.join(lista_palavras)
print(frase_unidas)