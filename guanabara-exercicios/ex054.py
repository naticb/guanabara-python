#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#maioridade e quantas já são maiores

from datetime import  date
atual = date.today().year
s = 0
p = 0
for c in range (1, 8):
    n = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if (atual - n) >= 21:
        s += 1
    else:
        p += 1
print('\n{} pessoas são maiores de idade e {} pessoas são menores de idade!'.format(s, p))
