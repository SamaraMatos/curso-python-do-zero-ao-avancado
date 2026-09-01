# função set()

# s1 = set() # set vazio
# s1={'samara', 1, 2, 3} #set com dados
# print(s1)

# l1= {1, 2, 3, 3, 3, 3, 3, 1} #set elimina 
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = set()
# s1.add('samara')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# # s1.discard('samara')
# # s1.discard('Olá mundo')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #uniao
s4 = s1 & s2 #intersecção itens presentes em ambos
s5 = s1 - s2 #diferanca itens presente apenas no set da esquerda
s6 = s2 - s1 
s7 = s1 ^ s2 # itens que não existe em ambos
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)


