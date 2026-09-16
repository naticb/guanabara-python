#Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 e 10. Só
# que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

#Minha resolução:
'''from random import randint
n = 20
r = 10
while n != r:
    n = int(randint(0, 10))
    r = int(input('Pensei em um valor de 0 a 5. Tente adivinhar... '))
    if n != r:
        print('Que pena! Você errou! Eu pensei no número {}'.format(n))
        print('Tente novamente!')
    else:
        print('Parabéns! Você acertou! Eu pensei no número {}'.format(n))'''

#Resolução Guanabara

from random import randint
computador = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou: #mesma coisa que 'while acertou == False:'
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez...')
        elif jogador > computador:
            print('Menos... Tente mais uma vez...')
print('Acertou com {} tentativas!'.format(palpites))
