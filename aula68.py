
x = 1

def escoto():
    global x #global torna o valor de x apartir de agora
    x = 10

    def outra_funcao():
        global x #usei novamente, então o valor de x e global apartir daq
        x = 11
        y = 2
        print(x,y)

    outra_funcao()
        
print(x)
escoto()
print(x)