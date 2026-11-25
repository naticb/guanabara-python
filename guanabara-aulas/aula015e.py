n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #comando break para a execução do while aqui
    s += n
print('A soma vale {}.'.format(s)) #esse resultado não soma o 999
#usando agora as novas f strings:
print(f'A soma vale {s}.')