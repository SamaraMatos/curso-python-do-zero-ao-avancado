def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista 

clientes1 = adiciona_clientes("Maria")
adiciona_clientes('joao', clientes1)
print(clientes1)