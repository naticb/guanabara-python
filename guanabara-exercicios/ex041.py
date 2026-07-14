#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SENIOR
#Acima: MASTER

idade = int(input('Qual a sua idade? '))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
