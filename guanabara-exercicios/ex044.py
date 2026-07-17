#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
#pagamento:
#À vista dinheiro/ cheque: 10% de desconto
#Á vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('Olá, considere essas condições de pagamento: \n'
      '1 - À vista dinheiro/ cheque: 10% de desconto\n'
      '2 - Á vista no cartão: 5% de desconto\n'
      '3 - Em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros\n')

preco = float(input('Digite o valor do produto em R$: '))
pagamento = int(input('Digite a forma de pagamento escolhida (1, 2, 3 ou 4): '))

if pagamento == 1:
    valor = preco*0.9
elif pagamento == 2:
    valor = preco*0.95
elif pagamento == 3:
    valor = preco
    print('Em duas vezes o valor da parcela será de R${} sem juros.'.format(valor / 2))
elif pagamento == 4:
    valor = preco * 1.2
    parcela = int(input('Quantas parcelas? '))
    print('Em {} vezes o valor da parcela será de R${:.2f} com juros.'.format(parcela,(valor / parcela)))
else:
    valor = '-INVÁLIDO-'
    print('Opção inválida, tente novamente.')

print('O preço final será R$ {}.'.format(valor))
