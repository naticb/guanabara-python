#O mesmo professor do desafio anterior quer sortear a ordem de apresentaão de trabalhados dos alunos.
#Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteada.

from random import  shuffle

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print (lista)
