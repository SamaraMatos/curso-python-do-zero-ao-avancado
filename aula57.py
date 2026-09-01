'''
lista de listas e seus índices
'''

salas = [
    ['MARIA', 'HELENA'],
         ['ELAINE',],
         ['LUIZ', 'JOAO', 'EDUARDA',],
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])



for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)