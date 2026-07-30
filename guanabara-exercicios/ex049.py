#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um valor inteiro: '))
print('-' * 12)
for c in range (1, 10):
    s = n * c
    print('{} x {} = {}'.format(n, c, s))
print('-' * 12)
