nome = 'Samara Matos'
altura = 1.58
peso = 56
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,' # f permite que use uma variavel no meu de uma str / :.2f arredondar  
linha_2 = f'Seu peso é {peso} quilos, e seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)