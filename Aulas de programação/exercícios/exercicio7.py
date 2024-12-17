"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_recebido = input('Digite um número inteiro: ')

try:
    if numero_recebido:
        numero = float(numero_recebido)
        if numero % 2 == 0:
            print('O número informado é par.')
        else:
            print('O número informado é ímpar.')
except:
    print('Você não informou um número inteiro.')
        

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_recebida = input('Por gentileza, diga o horário: ')
hora_f = float(hora_recebida)

if hora_f >= 0 and hora_f <= 11:
    print('Te desejo um bom dia! :D')
elif hora_f >= 12 and hora_f <= 17:
    print('Te desejo uma ótima tarde! :D')
elif hora_f > 17 and hora_f < 24:
    print('Te desejo uma ótima noite!. :D')    
else:
    print('Não reconheço este horário.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome, por favor: ')

if len(nome) <= 4:
    print('Seu nome é pequeno.')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')

# Uma forma de deixar o código acima mais limpo é:

nome = input('Digite o seu nome, por favor: ')
tamanho_nome = len(nome)


if tamanho_nome >1 and tamanho_nome <= 4:
    print('Seu nome é pequeno.')
elif tamanho_nome > 4 and tamanho_nome <= 6:
    print('Seu nome é normal.')
elif tamanho_nome > 6:
    print('Seu nome é grande.')
else:
    print('Por favor, digite um nome que contenha pelo menos mais de uma letra')