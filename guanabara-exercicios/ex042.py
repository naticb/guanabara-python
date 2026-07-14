#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: doislados iguais
#Escaleno: todos os lados diferentes

print('Vamos ver se forma triângulo!')
r1 = float(input('Escolha o tamanho do primeiro lado: '))
r2 = float(input('Escolha o tamanho do segundo lado: '))
r3 = float(input('Escolha o tamanho do terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, os segmentos acima podem formar triângulo!')
    if r1 == r2 and r2 == r3:
        print('Triângulo equilátero (todos os lados iguais)')
    elif r1 == r2 and r2 == r3 and r3 == r1:
        print('Triângulo isósceles (dois lados iguais)')
    else:
        print('Triângulo escaleno (todos os lados diferentes)')
else:
    print('Não, os segmentos acima não podem formar triângulo!')
