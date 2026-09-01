'''numero = input('Digite um número inteiro')

if numero.isdigit():
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0 
    par_impar_texto = 'impar'

    if numero_par:
       par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')       
else: 
   print('Voce não digitou um numero inteiro')
   '''




'''
   
entrada = input('digite que horas são:')
hora = int(entrada)

if hora >= 0 and hora <=11:
    print(f'Bom dia, são {hora} Hrs')
elif hora >= 12 and hora <=17:
    print(f'Boa Tarde, são {hora} Hrs')
elif hora >=18 and hora <= 23:
    print(f'Boa noite, são {hora} Hrs')
else:
    print('Não conheço essa hora')

'''
nome = input('Digite seu nome:')
qtd_letras = len(nome)

if qtd_letras > 1:
    if qtd_letras <= 4:
      print('Seu nome é muito curto')
    elif qtd_letras and 5 >= qtd_letras <= 6:
     print('Seu nome é normal')
    else:
        qtd_letras < 6 
        print('Seu nome é muito grande')
else:
   print('Digite mais de 1 letra')


