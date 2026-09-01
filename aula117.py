import json

pessoa = {
    'nome': 'Samara',
    'sobrenome': 'Matos',
    'endereco': [
        {'rua': 'rua 1', 'numero': 123},
        {'rua': 'rua 2', 'numero': 456},
],
    'Altura': 1.70,
    'numero_preferecido': [7, 3, 9],
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf-8') as arquivo: 
    json.dump(pessoa, arquivo, indent=2)  # Escreve o dicionário no arquivo JSON com indentação


with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa_carregada = json.load(arquivo)  # Carrega o conteúdo do arquivo JSON para um dicionário      
    print(pessoa_carregada['nome']) # Acessa o valor da chave 'nome' no dicionário carregado
    print(pessoa_carregada['sobrenome']) # Acessa o valor da chave 'sobrenome' no dicionário carregado
    print(pessoa_carregada['endereco']) # Acessa o valor da chave 'endereco' no dicionário carregado
    print(pessoa_carregada['Altura']) # Acessa o valor da chave 'Altura' no dicionário carregado
    print(pessoa_carregada['numero_preferecido']) # Acessa o valor