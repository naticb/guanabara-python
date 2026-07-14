#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex.: Ana Maria de Souza / primeiro: Ana / último: Souza

nome = str(input('Digite o nome completo: ')).strip()
d = nome.split()
print('Primeiro nome: {}'.format(d[0]))
print('Último nome: {}'.format(d[len(d)-1]))
