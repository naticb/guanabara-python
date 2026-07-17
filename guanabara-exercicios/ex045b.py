#Jogando jokenpo com o computador (resolvido guanabara)

from random import randint
from time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO...')
sleep(0.5)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador PEDRA
    if jogador == 0: # jogador PEDRA
        print('Empate!')
    elif jogador == 1: #jogador PAPEL
        print('Jogador venceu!')
    elif jogador == 2: #jogador TESOURA
        print('Computador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1: #computador PAPEL
    if jogador == 0: # jogador PEDRA
        print('Computador venceu!')
    elif jogador == 1: #jogador PAPEL
        print('Empate!')
    elif jogador == 2: #jogador TESOURA
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2: #jogou TESOURA
    if jogador == 0: # jogou PEDRA
        print('Jogador venceu!')
    elif jogador == 1: #jogou PAPEL
        print('Computador venceu!')
    elif jogador == 2: #jogou TESOURA
        print('Empate!')
    else:
        print('Jogada inválida!')
