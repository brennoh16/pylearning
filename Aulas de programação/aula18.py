# Como utilizar o sistema and

entrada = input('[E]entrar [S]sair')
senha_digitada = input('Senha: ')
senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')