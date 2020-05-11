#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
print('\033[31m-=\033[m' * 11)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
\033[33m[ 0 ]\033[m PEDRA
\033[31m[ 1 ]\033[m PAPEL
\033[33m[ 2 ]\033[m TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[33mJO\033[m')
sleep(1)
print('\033[31mKEN\033[m')
sleep(1)
print('\033[33mPÔ!!!\033[m')
sleep(1)
print('\033[31m-=\033[m' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[33m-=\033[m' * 11)
if computador == 0: #se computador jogou pedra
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[33mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('\03[31mJOGADA INVÁLIDA.\033[m')
if computador == 1: #se computador jogou papel
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[33mJOGADOR VENCEU!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
if computador == 2: #se o computador jogou tesoura
    if jogador == 0:
        print('\033[33mJOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
print('\033[31m-=\033[m' * 11)