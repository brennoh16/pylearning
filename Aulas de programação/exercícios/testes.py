# pares = []
# for x in range (1, 11):
#     if x % 2 == 0:
#         pares.append(x)
#         print(pares)

contador = 0
soma = 0

numero = float(input("Digite um número: "))

while True:
    soma += numero
    contador += 1
    numero = float(input('Digite outro número: '))

    if numero == 0:
        break

print(f'A soma dos números é {soma}.')
print(f'A quantidade de números somados foram: {contador}.')