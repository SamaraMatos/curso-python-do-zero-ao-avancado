'''
interador -> quem sabe entregar um valor por vez
next -> me entregue p proximo valor
iter -> me entregue seu interador
'''
#for letra in textp
texto = 'samara' #iteravel
iteratador = iter(texto) #iterador

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break


#acima é o que o for faz por baixo dos panos

# aqui é o for

texto = 'samara'
for letra in texto:
    print(letra)