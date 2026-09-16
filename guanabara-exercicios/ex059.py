#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
print('\n' + '-' * 8 + ' OPERAÇÕES MATEMÁTICAS ' + '-' * 8)
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = 10
while c != 5:

    print('''
    Menu:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    c = int(input('Digite a opção escolhida: '))
    if c == 1:
        print('\nO resultado é: {}'.format(a + b))
    elif c == 2:
        print('\nO resultado é: {}'.format(a * b))
    elif c == 3:
        if a > b:
            print('\nO maior é o {}'.format(a))
        elif a < b:
            print('\nO maior é o {}'.format(b))
        else:
            print('\nNão existe valor maior, os dois são iguais.')
    elif c == 4:
        a = int(input('\nDigite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
    elif c == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    sleep(2)
print('Fim do programa!')
