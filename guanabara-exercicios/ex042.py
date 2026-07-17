#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: doislados iguais
#Escaleno: todos os lados diferentes

print('Vamos ver se forma triângulo?')

r1 = float(input('Escolha o tamanho do primeiro lado: '))
r2 = float(input('Escolha o tamanho do segundo lado: '))
r3 = float(input('Escolha o tamanho do terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  #vamos usar condições aninhadas
    print('Sim, os segmentos acima podem formar um triângulo ', end='') #para juntar com os textos de tipo de triângulo
    if r1 == r2 == r3:           #eu tinha feito assim, também está certo -> r1 == r2 and r2 == r3:
        print('equilátero (todos os lados iguais)!')
    elif r1 != r2 != r3 != r1:   #aqui é importante fazer a comparação com r1 (exemplo digitando: 4 2 4)
        print('escaleno (todos os lados diferentes)!')
    else:
        print('isósceles (todos os lados iguais)!')
else:
    print('Não, os segmentos acima não podem formar um triângulo!')
