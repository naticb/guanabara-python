#Melhore o desafio 061, pergutando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerra quando ele disser que quer mostrar 0 termos.

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
total = 0
d = 10
while d != 0:
    total += d
    while c <= total:
        print(a)
        a += r
        c += 1
    d = int(input('Quer ver mais termos? Digite a quantidade: '))
print('Fim! Total: {} termos mostrados.'.format(total))
