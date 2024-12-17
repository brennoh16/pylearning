# Solicita ao usuário que digite uma frase
frase = input('Digite a frase: ')
 
# Inicializa o contador e variáveis para a letra que mais aparece e a quantidade de vezes que ela aparece
i = 0
qtd_vezes = 0
letra_apareceu_mais_vezes = ''
 
# Itera sobre cada caractere na frase
while i < len(frase):
    # Obtém o caractere atual da frase
    letra_atual = frase[i]
 
    # Ignora espaços em branco
    if letra_atual == ' ':
        i += 1
        continue
 
    # Conta quantas vezes a letra atual aparece na frase
    qtd_vezes_atual = frase.count(letra_atual)
 
    # Verifica se a quantidade atual é maior que a quantidade registrada anteriormente
    if qtd_vezes < qtd_vezes_atual:
        # Atualiza a quantidade e a letra que mais aparece
        qtd_vezes = qtd_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
 
    # Passa para o próximo caractere na frase
    i += 1
 
# Exibe a letra que mais aparece e quantas vezes ela apareceu
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_vezes} vezes'
)