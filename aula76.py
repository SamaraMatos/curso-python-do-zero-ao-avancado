# pessoa = {
#     'nome': 'Samara',
#     'sobremone': 'Matos',
#     'idade': 29,
#     'altura': 1.58,
#     'endereços': [
#         {'rua': 'Manoel Felipe', 'numero': 54},
#         {'rua': 'Morro Agudo', 'numero': 58,}
#     ]

# }
# for chave in pessoa:
#     print(chave, pessoa[chave])
#############################

# pessoa = {}


# chave = 'nome'

# pessoa[chave] = 'Samara'
# pessoa['sobrenome'] = 'Matos'

# print(pessoa[chave])

# pessoa[chave] = 'Leo'

# # del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])


# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])
#######################

# pessoa = {
#     'nome': 'Samara',
#     'sobrenome': 'Matos ', 
#     # 'Idade': 29,

# }
# pessoa.setdefault('idade', 54)#torna a chave 'idade' que nao existe no valor definido 54
# print(pessoa['idade'])#chave idade não existe, mas a função deffault tornou 54

# print(len(pessoa)) #retorna quantas chaves
# print(list(pessoa.keys())) # mostra a chave
# print(list(pessoa.values())) # mostra o valor
# print(list(pessoa.items())) #chave e valor

#####################
# d1 = {
#     'c1': 1,
#     'c2': 2,
    
# }
# d2 = d1.copy() #d2copia o dict do d1, porém ao musar o valor do d2, o d1 continua com seu valor de inicio
# d2['c1'] = 1000

# print(d1)
# print(d2)
#######################

p1 = {
    'nome': 'Samara',
    'Sobrenome': 'Matos',
}


# print(p1.get('nome')) #get obtem o valor da chave 'nome'

# nome = p1.pop('nome') #apaga o item com a chave especificada
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() #apaga o ultimo item adicionado
# print(ultima_chave)
# print(p1)

p1.update(nome='emerson', idade = 54) #atualiza com os valores adionados
print(p1)


# for chave in pessoa:
#     print(chave)