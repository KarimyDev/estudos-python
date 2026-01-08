'''
enumerate - enumera iteráveis (índices)
'''
lista = ['Maria','Helena','Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

print('O que tem na lista enumerada:', lista)

for item in lista_enumerada:
    print(f'\t{item}')

#       OU

lista2 = ['Maria','Helena','Luiz']
lista2.append('João')

for indice, nome in enumerate(lista2):
    print(indice, nome)

#       OU

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
