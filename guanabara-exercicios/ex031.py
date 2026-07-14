#Desenvolva um programa que pergunte a distância de uma viagem em km
#Calcule o preço da passagem, cobrando R$ 0,5 por km, para viagens de até 200km e R$ 0,45 para viagens mais longas

km = float(input('Qual a distância em km? '))

#MINHA RESOLUÇÃO
'''if km <= 200:
    print('O valor da viagem é de R${:.2f}.'.format(km * 0.5))
else:
    print('O valor da viagem é de R${:.2f}.'.format(km * 0.45))'''

#RESOLUÇÃO ALTERNATIVA COM IF INLINE OU OPERADOR TERNÁRIO
p = km * 0.5 if km <= 200 else km * 0.45
print('O valor da viagem é de R${:.2f}.'.format(p))
