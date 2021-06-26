# Vamos jogar JOKENPÔ!!
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') # opções dos jogadores!
cp = randint(0,2)
print('Ola, eu me chamo \33[35mKaila\33[m, vamos jogar JOKENPÔ')
print('''Suas opções são:
\33[34m[0] PEDRA
[1] PAPEL
[2] TESOURA\33[m''')
jog = int(input('\33[32mQual é a sua jogada? \33[m'))
print('\33[33mJO\33[m')
sleep(1)
print('    \33[35mKEN\33[m')
sleep(1)
print('        \33[31;402mPO!!!!!\33[m')
print('-=' * 12)
print('Eu joguei \33[35m{}!!\33[m'.format(itens[cp]))
print('\33[34mVocê\33[m jogou \33[36m{}!!\33[m'.format(itens[jog]))
print('-=' * 12)
if cp == 0: # computador jogou PEDRA
    if jog == 0:
        print('\33[31mEMPATE!!\33[m')
    elif jog == 1:
        print('JOGADOR VENCE!')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!!')
elif cp == 1: # computador jogou PAPEL
    if jog == 0:
        print('COMPUTADOR VENCE!')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE!!')
    else:
        print('JOGADA INVÁLIDA!!')
elif cp == 2: # computador jogou TESOURA
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!!')





