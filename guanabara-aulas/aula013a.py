for c in range(1, 6): #faz do 1 até o 5 e no 6 ele para
    print('Oi')
print('FIM\n') #aqui a identação do código faz toda a diferença

for c in range (1, 7):
    print(c)
print('FIM\n')

for c in range (6, 0):
    print(c)
print('FIM\n')
#no caso acima, ele não executa nada do for. Portanto, caso queira contar para trás fica:

for c in range (6, 0, -1): # o menos 1 diz o que faz no final de cada repetição
    print(c)
print('FIM\n')

for c in range (0, 7, 2): #pulou 2
    print(c)
print('FIM\n')
