n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s)) #o resultado dessa soma considera o 999, pois o comando do while acontece até o final