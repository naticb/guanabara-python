n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('FIM\n')

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for c in range (inicio, fim+1, passo):
    print(c)
print('FIM\n')

for c in range (0, 3):
    teste = int(input('Digite um valor: '))
print(teste)
print('FIM\n')

s = 0
for c in range (0, 4):
    g = int(input('Digite umm valor: '))
    s +=g #é a mesma coisa que: s = s + g
print('O somatório de todos os valores foi {}\n'.format(s))
