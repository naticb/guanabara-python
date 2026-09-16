# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1 = 120

#Minha resolução
'''n = int(input('Digite um valor para calcular o fatorial: '))
c = n
f = n
t = str(n) + '! = '
while c > 1:
    c -= int(1)
    f = f * c
    t = t + str(c) + ' x '
print(t)
print(f)'''

#Resolução simples guanabara
'''from math import factorial
n = int(input('Digite um valor para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

#Resolução usando o while guanabara
n = int(input('Digite um valor para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
