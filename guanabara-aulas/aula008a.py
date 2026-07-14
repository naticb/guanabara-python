from math import sqrt, floor #para importar algo específico
#import math (para importar tudo, na linha 5 por ex, usar 'raiz = math.sqrt(num)')
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
