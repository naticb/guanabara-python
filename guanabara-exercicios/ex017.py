#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente e mostre o valor da hipotenusa

'''co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** (1/2)
print('O cateto oposto vale {} e o cateto adjacente vale {}.\nSendo assim, a hipotenusa vale {:.2f}'.format(co, ca, h))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}.'.format(hi))


