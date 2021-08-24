# O jogo com a inclusão do aúdio e cores, tem como objetivo  torna-lo mais interativo e divertido
from random import randint
import pyttsx3
engine = pyttsx3.init()
v = 0
nome = str(input('Qual o seu nome?: ')).strip()
engine.say(f'Olá{nome} eu sou a Kaila, vamos jogar PAR OU ÌMPAR?')
engine.runAndWait()
while True:
    jog = int(input('Digite um valor: '))
    comp = randint(0, 10)
    tl = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    print(f'{nome}, Você jogou \33[33m{jog}\33[m e Eu \33[34m{comp}\33[m. O total foi: \33[31m{tl}\33[m ', end='')
    print('Deu PAR!!'if tl % 2 == 0 else 'Deu ÍMPAR!!')
    if tipo == 'P':
        if tl % 2 == 0:
            print('\33[32mVocê VENCEU!!\33[m')
            engine.say('Não vai se achando não tá!')
            engine.runAndWait()
            v += 1
        else:
            print('\33[33mVocê PERDEU !!\33[m')
            engine.say('Chora não bebê!!')
            engine.runAndWait()
            break
    elif tipo == 'I':
        if tl % 2 == 1:
            print('\33[32mVocê Venceu!!\33[m')
            engine.say('Não vai se achando não tá!')
            engine.runAndWait()
            v += 1
        else:
            print('\33[33mVocê PERDEU!!\33[m')
            engine.say('Chora não bebê!!')
            engine.runAndWait()
            break
    print('\33[34mVamos jogar novamente...\33[m')
print(f'\33[31mGAME OUVER!\33[m Você venceu\33[35m {v}\33[m vezes')
engine.say('Mais sorte na próxima vez! hahaha!')
engine.runAndWait()
















