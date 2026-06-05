#crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira

import math
n = float(input('Digite um número do tipo float: '))
print('A parte inteira deste valor é {}.'.format(math.trunc(n)))

#outra maneira de resolver sem importar bibliotecas:
'''num = float(input('Digite um valo: '))
print('A parte inteira deste valor é {}.'.format(int(num)))'''
