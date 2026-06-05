#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

#MINHA RESOLUÇÃO
'''ano = str(input('Digite o ano: '))

if int(ano[2:4]) == 0:
    if (int(ano) % 400) > 0:
        print('Não, o ano {} não é um ano bissexto!'.format(ano))
    else:
        print('Sim, o ano {} é um ano bissexto!'.format(ano))
else:
    if (int(ano[2:4]) % 4) > 0:
        print('Não, o ano {} não é um ano bissexto!'.format(ano))
    else:
        print('Sim, o ano {} é um ano bissexto!'.format(ano))'''

#RESOLUÇÃO GUANABARA
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #pegando o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #regra completa
    print('Sim, o ano {} é bissexto.'.format(ano))
else:
    print('Não, o ano {} não é bissexto.'.format(ano))
