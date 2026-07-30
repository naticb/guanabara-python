#desafio 48 resolvido pelo professor guanabara

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c #soma recebe ele mesmo mais c
        cont += 1 #cont recebe ele mesmo mais um
print('A soma de {} valores solicitados é {}'.format(cont, soma))
