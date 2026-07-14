#faça um programa que leia um angulo qualquer e moststre o valor do seno, do cosseno e da tangente

from math import sin, cos, tan, radians
a = float(input('Digite um angulo: '))
an = radians(a)
print('Para o ângulo {:.2f}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a, sin(an),cos(an), tan(an)))
