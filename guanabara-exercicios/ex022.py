#Crie um programa que leia o nome completo de uma pessoa e mostre:
from os.path import split
from shlex import join

#O nome com todas as letras minúsculas
#O nome com todas as letras maiúsculas
#Quantas letras ao todo, sem considerar espaços
#Quantas letras tem o primeiro nome

#MEU JEITO
'''nome = str(input('Digite o nome completo: '))

print('Nome com letras minúsculas: {}'.format(nome.lower()))
print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Quantidade de letras: {}'.format(len(''.join(nome.split()))))

dividido = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], len(dividido[0])))'''

#Resolução guanabara
nome = str(input('Digite o nome completo: ')).strip()
print('Nome com letras minúsculas: {}.'.format(nome.lower()))
print('Nome com letras maiúsculas: {}.'.format(nome.upper()))
print('Quantidade de letras: {}'.format(len(nome)-nome.count(' '))) #total do nome menos o total de espaços
print('Quantidade de letras no primeiro nome: {}.'.format(nome.find(' '))) #encontrando o primeiro espaço, ou seja, o tamanho do primeiro nome
