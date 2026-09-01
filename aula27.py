'''
fatiamento de strings
012345678
olá mundo
-987654321
fatiamento [i:f:p] [::] i-inicio f-fim p-passo
obs: a funçao len retorna a qtd de carat da str
'''
variavel = 'olá mundo'
print(variavel[4:])
print(variavel[0:5])
print(len(variavel))
print(variavel[0:9:3]) # 3 eé o passo pula me  em 3
print(variavel[::-1])