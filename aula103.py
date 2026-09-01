def inverte_string(string):
    return string[::-1]



invertida = inverte_string('samara')
print(invertida )
'''

🎯 O que é um decorador?

Um decorador é uma função que modifica o comportamento de outra função sem alterar o código da função original.

É como colocar uma “camada extra” ao redor da função.

Imagine:

Entrada → Função decorada → Saída


Ou ainda:

decorador(função_original) → nova_função

🧩 Como funciona por dentro?

Decorador = função que recebe uma função e retorna outra.

Exemplo simples:

def decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("Depois")
    return wrapper


Aqui acontece:

decorador recebe uma função (func)

cria outra função (wrapper) que faz algo extra

retorna wrapper

essa nova função substitui a função original

🔌 Como usar? Com a notação @
@decorador
def minha_funcao():
    print("Função original")


Isto é igual a:

minha_funcao = decorador(minha_funcao)
'''