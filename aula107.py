def unir_lista(cidades, estados):
    return [(c, e) for c, e in zip(cidades, estados)]
        
    

list_cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_estados = ['BA', 'SP', 'MG', 'RJ']

resultado = unir_lista(list_cidade, list_estados)
print(resultado)


