#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
num = int(randint(0,5))
#print('pensei no {}'.format(num))
chute = int(input('Pensei em um valor entre 0 e 5. Tente adivinhar... '))
print('E o resultado do jogo é...')
sleep(2) #esperado 3 segundos
if num == chute:
    print('Parabéns, você acertou! O valor que escolhi foi o {}.'.format(num))
else:
    print('Que pena, você errou! O valor que escolhi foi o {}.'.format(num))
