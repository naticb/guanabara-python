#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a
#tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

altura = float(input('Digite a altura em metros: '))
peso = float(input('Digite o peso em kg: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('IMC é {:.2f}, abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC é {:.2f}, peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC é {:.2f}, sobrepeso.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('IMC é {:.2f}, obesidade.'.format(imc))
else:
    print('IMC é {:.2f}, obesidade mórbida'.format(imc))
