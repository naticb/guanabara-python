#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo

ano = int(input('Digite o ano de nascimento: '))
idade = 2026 - ano

if idade > 18:
    print('Já passou {} ano(s) do tempo de alistamento!'.format(idade - 18))
elif idade == 18:
    print('Você tem {} anos! Está na hora de se alistar!'.format(idade))
else:
    print('Em {} ano(s), você deve se alistar!'.format(18 - idade))
