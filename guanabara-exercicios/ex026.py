#Faça um programa qe leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite a frase: ')).lower().strip()
print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('a')+1)) #rfing para achar a última posição
