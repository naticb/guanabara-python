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
else:
    valor = preco*1.2

print('Ok, o preço final do seu produto fica R$ {}!'.format(valor))
