#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
#casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa em R$? '))
salario = float(input('Qual o valor do seu salário em R$? '))
anos = int(input('Em quantos anos pretende pagar a casa? '))
parcela = valor / (anos * 12)

print('A prestação fica no valor de R${:.2f}'.format(parcela))

if parcela > 0.3 * salario:
    print('Que pena! Empréstimo negado!')
else:
    print('Parabéns! Empréstimo concedido!')
