import random

# Aqui nos podemos gerar um número aleátorio
# importando da biblioteca random.
 
numero_secreto = random.randint(1, 10)

# Essa variável define a quant. de palpites
palpites = 3

print(
    f"Você tem 3 palpites, tente advinhar o número entre 1 e 10")

# loop de tentativas
tentativa = 1
while tentativa <= palpites:
    
    palpite = int(input(f"Tentativa {tentativa} de {palpites}: "))
    
    # Verificar o palpite
    if palpite is not numero_secreto:
        print("Você errou. Tente novamente!")
    elif palpite > numero_secreto:
        print("Você errou. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto}!")
        break
    
    tentativa += 1

if palpite != numero_secreto:
    print(f"Você não acertou. O número secreto era {numero_secreto}.")


