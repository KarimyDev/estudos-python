'''
Introdução ao desempacotamento + tuples (tuplas)
Tipo tupla - Uma lista imutável
'''
# _, nome, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome)

nomes = ['Maria', 'Helena', 'Luiz']
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)

'''
Desempacotamento em chamadas de métodos e funções
'''
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, ap, u = lista
print(p, u, ap)

#for nome in lista:
#    print(nome, end=' ', sep=' ')

print(*lista)
print(*string)
print(*tupla)
