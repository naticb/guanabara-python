#Crie um programa que faça o computador jogar Jokênpo com você

from random import choice

v1 = 'Pedra'
v2 = 'Papel'
v3 = 'Tesoura'

lista = [v1, v2, v3]
pc = choice(lista)
resposta = input('Escolha pedra, papel ou tesoura: ')
pessoa = resposta.capitalize()

if pc == 'Pedra':
    if pessoa == 'Papel':
        print('Ganhou! Eu escolhi {}!'.format(pc))
    elif pessoa == 'Tesoura':
        print('Perdeu! Eu escolhi {}'.format(pc))
    elif pessoa == 'Pedra':
        print('Empatou! Eu escolhi {}'.format(pc))
    else:
        print('Resposta inválida, tente novamente!')
elif pc == 'Papel':
    if pessoa == 'Tesoura':
        print('Ganhou! Eu escolhi {}!'.format(pc))
    elif pessoa == 'Pedra':
        print('Perdeu! Eu escolhi {}'.format(pc))
    elif pessoa == 'Papel':
        print('Empatou! Eu escolhi {}'.format(pc))
    else:
        print('Resposta inválida, tente novamente!')
else:
    if pessoa == 'Papel':
        print('Perdeu! Eu escolhi {}!'.format(pc))
    elif pessoa == 'Pedra':
        print('Ganhou! Eu escolhi {}'.format(pc))
    elif pessoa == 'Tesoura':
        print('Empatou! Eu escolhi {}'.format(pc))
    else:
        print('Resposta inválida, tente novamente!')
