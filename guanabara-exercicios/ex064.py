#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 0
s = 0
t = 0
while c != 999:
    c = int(input('Digite um valor: '))
    s += c
    t += 1
print('Você digitou {} números e a soma deles é {}.'.format(t - 1, s - 999))
print('FIM!')
