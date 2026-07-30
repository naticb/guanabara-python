#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplo: apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper() #ler a frase e tirar os espaços antes e depois, deixar todas maiúsculas
palavras = frase.split() #transformar as palavras em uma lista
junto = ''.join(palavras) #juntar tudo, para tirar os espaços
inverso = ''
for letra in range (len(junto) - 1, -1, -1): #temos que fazer len - 1, pq o tamanho da palavra será sempre contando um a mais
    inverso += junto[letra] #inverso ganha as letras de forma invertida, usando o junto na posição letra
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
