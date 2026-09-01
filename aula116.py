import os
caminho_arquivo =  'aula116.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(['Linha 3\n', 'Linha 4\n', 'Linha 5\n'])  # Escreve uma lista de linhas no arquivo
    arquivo.seek(0,0) # Mover o cursor para o início do arquivo
    print(arquivo.read())  # Mover o cursor para o início do arquivo

print('---' * 10)
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

#os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula116_renomeado.txt')