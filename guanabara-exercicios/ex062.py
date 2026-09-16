#Melhore o desafio 061, pergutando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerra quando ele disser que quer mostrar 0 termos.

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    a += r
    c += 1
    print(a)
    d = int(input('Quer ver mais termos? Digite a quantidade: '))
    if d != 0:
        while c <= d:
            a += r
            print(a)
            c += 1
