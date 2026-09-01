'''
CONSTANTE ='Variáveis' que não vão mudar
Muitas condiçoes no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
'''

velocidade = 61 # VELOCIDADE ATUAL DO CARRO
local_carro = 101 #LOCAL EM QUE O CARRO ESTÁ NA ESTRADA

RADAR_1 = 60 # VELOCIDADE MAÁXIMA DO RADAR 1
LOCAL_1 = 100 # LOCAL ONDE O RADAR 1 ESTÁ
RADAR_RANGE = 1 # A DISTâNCIA ONDE O RADAR PEGA

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade que o carro passou no radar1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('O carro foi multado no radar 1')