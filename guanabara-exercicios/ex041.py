#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SENIOR
#Acima: MASTER

from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
idade = atual - ano

print('Sua idade é {}'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
