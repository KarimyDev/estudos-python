n = int(input("Quantos numeros serao digitados? "))

vet: [float] = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero: "))

print()
print("Valores = ", end="")
for i in range(0,n):
    print(f"{vet[i]:.1f} ", end="")

print()
soma = 0
for i in range(0,n):
    soma = soma + vet[i]

print(f"Soma = {soma:.2f}")

media = soma / n
print(f"Media = {media:.2f}")
