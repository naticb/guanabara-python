#desafio 51 resolvido pelo professor guanabara

primeiro = int(input('Primeiro termo: '))
razao  = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao #formula matemática para achar o valor de um termo, no caso, o décimo termo
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end = '-> ')
print('ACABOU')
