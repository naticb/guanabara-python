#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
#a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Média {:.2f} | REPROVADO'.format(media))
elif 5.0 >= media or media <= 6.9:
    print('Média {:.2f} | RECUPERAÇÃO'.format(media))
else:
    print('Média {:.2f} | APROVADO'.format(media))
