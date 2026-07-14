d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Qual a quantidade de km rodado? '))
preco = (d * 60) + (km * 0.15)
print('O valor total a pagar é de R${:.2f}'.format(preco))
