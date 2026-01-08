# if /    elif   /  else
# se / se não se / se não

entrada = input("Você quer 'entrar' ou 'sair'? ")

if entrada == 'entrar':
    print("Você entrou no sistema")

elif entrada == 'sair' :
    print("Você saiu do sistema")

else :
    print("Você não digitou nem 'entrar' nem 'sair'.")

print("FORA DOS BLOCOS")

'''
numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')
'''
