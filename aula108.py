# def soma_listas(a, b):
#     return [a + b for a, b in zip(a, b)]/ 

# valores_1 = [1, 2, 3, 4, 5, 6, 7]
# valores_2= [1, 2, 3, 4]

# res = soma_listas(valores_1, valores_2)
# print(res)
#####################################



# valores_1 = [1, 2, 3, 4, 5, 6, 7]
# valores_2= [1, 2, 3, 4]

# lista_soma = []
# for a, b in zip(valores_1, valores_2):
#     lista_soma.append(a + b)
# print(lista_soma)
######################################

valores_1 = [1, 2, 3, 4, 5, 6, 7]
valores_2= [1, 2, 3, 4]

lista_soma = [a + b for a, b in zip(valores_1, valores_2)]
print(lista_soma)
