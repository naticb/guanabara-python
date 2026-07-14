#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo
from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano

if idade > 18:
    print('Você tem {} anos! Já passou {} ano(s) do tempo de alistamento!'.format(idade, idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
elif idade == 18:
    print('Você tem {} anos! Está na hora de se alistar!'.format(idade))
else:
    print('Você tem {} anos! Em {} ano(s), você deve se alistar!'.format(idade, 18 - idade))
    print('O seu alistamento será em {}.'.format(ano + 18))
