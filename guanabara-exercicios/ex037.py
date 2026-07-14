#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

n = int(input('Digite um valor inteiro: '))
print('Base de conversão:\n 1 - Binário\n 2 - Octal \n 3 - Hexadecimal')
c = int(input('Digite a base de conversão escolhida: '))

if c == 1:
    b = 'Binário'
    print('{} convertido para binário é igual a {}.'.format(n, bin(n)[2:])) #[2:] é o fatiamento
elif c == 2:
    b = 'Octal'
    print('{} convertido para octal é igual a {}.'.format(n, oct(n)[2:]))
elif c == 3:
    b = 'Hexadecimal'
    print('{} convertido para hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida! Escolha 1, 2 ou 3.')
