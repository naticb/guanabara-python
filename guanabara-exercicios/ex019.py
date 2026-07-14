#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O nome sorteado foi {}.'.format(escolhido))
