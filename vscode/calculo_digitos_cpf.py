"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf_enviado_usuario = input('Digite os nove primeiros dígitos do seu CPF -(somente números): ')
cpf_enviado_usuario = ''.join(filter(str.isdigit, cpf_enviado_usuario))  
# Remove caracteres não numéricos

# Verifique se o CPF tem exatamente 9 dígitos e é numérico
if len(cpf_enviado_usuario) != 9 or not cpf_enviado_usuario.isdigit():
    print('CPF inválido! Você deve digitar exatamente 9 dígitos numéricos.')
else:
    nove_digitos = cpf_enviado_usuario[:9]
    contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'Primeiro dígito é: {digito_1}')

"""
Calculo do segundo dígito do CPF
CPF: 461.110.418-43
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  461.110.418-43 (4611104184)
   11 10  9  8  7  6  5  4  3  2
*  4   6  1  1  1  0  4  1  8  4 <-- PRIMEIRO DIGITO
   44  60 9  8  7  0  20 4  24 8

Somar todos os resultados:
44+60+9+8+7+0+20+4+24+8 = 184
Multiplicar o resultado anterior por 10
184 * 10 = 1840
Obter o resto da divisão da conta anterior por 11
1840 % 11 = 3
Se o resultado anterior for maior que 9:
    resultado é 3
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 3
"""

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'Segundo dígito é: {digito_2}')


cpf_completo = f'{nove_digitos}{digito_1}{digito_2}'
cpf_formatado = (f'{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}')

print(f'Seu CPF é: {cpf_formatado}')
