""" Calculadora com while """

while True:
    # Aqui nós temos o recebimento de dados do usuário:

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador(+-*/): ')

    # Aqui nos criamos uma flag para realizar as verificações do programa:

    numeros_validos = None

    # Utilizamos o try and except para verificar se os dados recebidos são válidos.

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Algum dos números informados não é válido.')
        continue

    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Você digitou um operador inválido.')
        continue

    #Aqui foi utilizado o len para caso o usuário digita mais de 1 operador.

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # Aqui são os códigos das operações matemáticas:

    print('Realizando sua conta, confira o resultado abaixo:')
    # if operador == '+':
    #     soma = num_1_float + num_2_float
    #     print(soma)
    # elif operador == '-':
    #     subtração = num_1_float - num_2_float
    #     print(subtração)
    # elif operador == '*':
    #     multiplicação = num_1_float * num_2_float
    #     print(multiplicação)
    # elif operador == '/':
    #     divisão = num_1_float // num_2_float
    #     print(divisão)
    match operador:
        case '+':
            print(f'Sua soma é {num_1_float + num_2_float}.')
        case '-':
            print(f'Sua subtração é: {num_1_float - num_2_float}.')
        case '*':
            print(f'Sua multiplacão é: {num_1_float * num_2_float}')
        case '/':
            print(f'Sua divisão é: {num_1_float // num_2_float}.')

    # Caso o usuário deseje sair do programa:
    sair = input('Você deseja sair? [S]im.').upper().startswith('s')
    
    if sair is True:
        print('Até mais.')
        break


    


        


        



