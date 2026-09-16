# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um valor inteiro: '))
c = n
f = n
t = str(n) + '! = '
while c > 1:
    c -= int(1)
    f = f * c
    t = t + str(c) + ' x '
print(t)
print(f)
