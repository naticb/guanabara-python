#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo

print('Analisador de Triângulos\n')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, os segmentos acima podem formar triângulo!')
else:
    print('Não, os segmentos acima não podem formar triângulo!')
