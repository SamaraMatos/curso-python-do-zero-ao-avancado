'''
primeiro digito
cpf = 09486370990
0  9  4  8  6  3  7  0  9
10 9  8  7  6  5  4  3  2
10 81 32 56 36 15 28 3  18 


soma = 266
266 * 10 = 2600
2600 % 11 = 4
'''
import random
for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado = 0 
    for digito in nove_digitos:
        resultado += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = ((resultado * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0


    '''
    segundo digito 
    0  9  4  8  6  3  7  0  9  9
    11 10 9  8  7  6  5  4  3  2
    11 90 36 64 42 18 35 4 27 18
    345*10= 3450
    3450 % 11 = 7
    '''
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_2 = 0 
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = ((resultado_2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0


    novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

    print(novo_cpf)