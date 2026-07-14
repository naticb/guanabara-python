#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
#mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite

vel = float(input('Qual é a velocidade do carro em Km/h? '))
if vel > 80:
    print('Não permitido, velocidade acima de 80Km/h! \nA multa será de R$ {}.'.format((vel-80)*7))
else:
    print('Boa viagem! Digija com segurança!')
