"""
Iterando strings com while
"""
#012345678910

nome = input('Digite o seu nome: ')
tam_nome = len(nome)
novo_nome = ''
contador = 0

while contador < tam_nome:
    novo_nome += nome[contador]
    novo_nome += '*'
    contador += 1

print(novo_nome)