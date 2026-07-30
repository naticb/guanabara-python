#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

max = 0
min = 0
for c in range (1, 6):
    p = float(input('Digite o peso da {}° pessoa em kg: '.format(c)))
    if c == 1: #considerando que é a primeira interação
        max = p
        min = p
    else:
        if p > max:
            max = p
        if p < min:
            min = p
print('O maior peso lido foi de {}kg '
      '\nO menor peso lido foi de {}kg'.format(max, min))
