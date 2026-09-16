#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja
#errado, peça a digitação novamente até ter um valor correto.

#Minha resolução:

'''s = 'fm'
while s not in 'F, M':
    s = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if s not in 'F, M':
        print('Tente novamente!\n')
    else:
        print('Ok, o sexo é {}'.format(s))'''

#Resolução Guanabara:

s = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while s not in 'F, M':
    s = str(input('Dados inválidos, digite novamente [M/F]: ')).strip().upper()[0]
print('Ok, valor registrado!')
