#exemplo uso sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'L' in letras:
        print('Achou')
        break

    print(letras)