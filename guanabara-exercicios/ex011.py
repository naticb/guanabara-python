a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
area = a * l
tinta = area / 2
print('A área da sua parede é {} m².'.format(area), end=' ')
print('Portanto, você vai precisar de {} litros de tinta.'.format(tinta))
