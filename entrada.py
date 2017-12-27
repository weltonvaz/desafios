import os
os.system('cls' if os.name == 'nt' else 'clear')

entrada = input('Digite codigo: ')
codigo = entrada.split(' ')

decode = ''.join(list(map(chr, map(lambda x: int(x, 2), codigo))))

print(decode)