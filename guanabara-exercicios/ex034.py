#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para salários inferiories ou iguais, o aumento é de 15%.

s = float(input('Qual o seu salário em R$? '))
if s > 1250:
    print('O seu aumento é de {}%, portanto, o seu novo salário é de: R${:.2f}'.format(10, s*1.1))
else:
    print('O seu aumento é de {}%, portanto, o seu novo salário é de: R${:.2f}'.format(15, s*1.15))
