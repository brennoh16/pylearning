#Equação do segundo grau

print('Calculando raízes do segundo grau\n')

# ax^2 + bx + c = 0

a = float(input('Informe qual o coeficiente a: '))
b = float(input('Informe qual o coeficiente b: '))
c = float(input('Informe qual o coeficiente c: '))

# Checando se é do primeiro grau
if a == 0:
    print('Essa função é do primeiro grau.')
    resultado = -c/b
    print(f'O resultado é {resultado}.')
    exit()

# Calculando o delta

delta = b**(2) - 4*a*c

# Checar se possui valores reais

if delta < 0:
    print('Essa equação não possui raízes reais.')
    exit()

elif delta == 0:
    raiz = -b / (2*a)
    print(f'A equação possui raiz única: {raiz}')

else:
    raiz1 = (-b + delta**(1/2) / (2*a))
    raiz2 = (-b - delta**(1/2) / (2/a))
    print(f'As raízes são: X1 = {raiz1} e {raiz2}')
