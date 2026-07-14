frase = 'Curso em Vídeo Python'
# nos pequenos espaços de memória do python, essa string fica armazenada desta forma:
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í]  [d]  [e]  [o]  [ ]  [P]  [y]  [t]  [h]  [o]  [n]
# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

print(frase)

print('-' * 12)
print('#posição 3 da string')
print(frase[3])

print('\n#range de 3 até 13, mas não traz o último valor')
print(frase[3:13])

print('\n#início até 13, mas não traz o último valor')
print(frase[:13])

print('\n#do 13 até o final')
print(frase[13:])

print('\n#do 1 até o 15, ele coloca um espaço')
print(frase[1:15])

print('\n#mostra um valor e pula dois, do 1 até o 15')
print(frase[1:15:2])

print('\n#mostra um valor e pula dois, do 1 até o final')
print(frase[1::2])

print('\n#mostra um valor e pula dois, do início ao final')
print(frase[::2])

print('-' * 12)

print('#formas de usar a aspas triplas')

print (''' texto longo
tão longo
com várias linhas''')

print('-' * 12)
print('#no python, maiúsculo e minúsculo são diferentes:')
print(frase.count('o'))
print(frase.count('O'))

print('-' * 12)
print('#contar a letra O jogando todas a frase para maiúsculo:')
print(frase.upper().count('O'))

print('-' * 12)
print('#Usando: len, strip')
frase2 = '   Curso em Vídeo Python   '
print(len(frase))
print(len(frase2))
print(len(frase2.strip())) #retirando espaços do início e do final

print('-' * 12)
print('#Usando: replace')
print(frase.replace('Python', 'Android'))
print(frase) #mostrando que ele não altera/ salva os resultados. Para alterar/salvar eu precisaria fazer: frase = frase.replace('Python', 'Android')

print('-' * 12)
print('#Usando: in, find, lower, capitalize')
print('#verifica se existe Curso na frase')
print('Curso' in frase) #retorna true ou false

print('\n#usando o capitalize')
print(frase.capitalize()) #deixa somente a primeira letra maiúscula

print('\n#retorna a posição de Curso na frase e -1 se não encontrar')
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('curso')) #procurando dentro da frase jogada para minúsculo

print('-' * 12)
print('#Usando: split, chamando isso de dividido e usando o join')
dividido = frase.split()
print(dividido)

print('\n#mostrando a posição 0 do dividido')
print(dividido[0])

print('\n#mostrando a posição 3, da posição 2 do dividido')
print(dividido[2][3])

print('\n#mostrando o dividido com join usando o traço')
print('-'.join(dividido))
