# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  K A R I M Y
# -6-5-4-3-2-1

nome = 'Karimy'
print(nome[2])
print(nome[-4])
print('imy' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

'''
nome = 'Maria Carmo'
 
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')
'''
