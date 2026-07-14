#Crie um programa uqe leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

#MINHA RESOLUÇÃO
cidade = input('Digite a cidade: ')
d = cidade.upper().split() # o split divide o texto onde houver espaços e remove e ignora completamente todos os espaços extras do início e do fim do texto
print('SANTO' in d[0])

'''OBS.:Se o usuário simplesmente não digitar nada e apenas apertar Enter (ou digitar apenas espaços), o .split() vai gerar uma lista totalmente vazia: [].
Quando o seu código tentar ler a posição zero dessa lista vazia (d[0]), o Python vai dar um erro na tela chamado IndexError: 
list index out of range (Erro de índice fora do intervalo), porque a posição 0 não existe. No código do Guanabara, se o usuário não digitar nada, ele apenas retorna False sem quebrar o programa.'''

#RESOLUÇÃO GUANABARA
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
