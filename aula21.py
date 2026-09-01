#operações logicas
# and (e) 
# and todos as condeçoes precisam ser verdadeiras
# se qualquer valor for considerado falso a expressão inteira avaliada naquele valor

entrada = input('[E]ntrar [S]air')
senha_digitada = ()
senha_permitida = '123456'

#if True

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')

print( True and False and True) # qualquer false é avaliado como false # 0 é false