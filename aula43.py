'''
texto = 'Python'
i = 0
tamanho_str = len(texto)

while i < tamanho_str:
    print(texto[i])

    i += 1

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('aquele laço acima pode ter repetiçoes infinitas')  
#while usamos quando não sabemos a qtd de repeções
'''
## FOR
texto = 'Python'

novo_texto = ''
# for = para / ex: para cada letra em  texto
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)

