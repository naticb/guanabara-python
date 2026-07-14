n = input('Digite algo: ')
print('O tipo primitivo deste valor é ', type(n))
print('É numérico? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está só em maiúsculas? ', n.isupper())
print('Está só em minúsculas? ', n.islower())
print('Está capitalizado? ', n.istitle()) #maiúscula + minúscula
