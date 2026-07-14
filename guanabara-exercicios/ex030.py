#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

num = int(input('Digite um número inteiro: '))
d = num % 2
if  d > 0:
    print('O número é ímpar!')
else:
    print('O número é par!')
