def number(prompt):
    while True:
        entrada = input(prompt)
        try:
            return int(entrada)
        except ValueError:
            print('O valor digitado não é um número. [TENTE NOVAMENTE]')

print('CALCULADORA SIMPLES')
print('''
Escolha um operador:
Digite [1] para adição (+)
Digite [2] para subtração (-)
Digite [3] para multiplicação (*)
Digite [4] para divisão (/)
''')

while True:
    operador_number = number('Escolha o operador: ')

    if operador_number not in (1, 2, 3, 4):
        print('Opção inválida. [Escolha um número entre 1 e 4]')
        continue

    numero_1 = number('Digite o primeiro número da operação: ')
    numero_2 = number('Digite o segundo número da operação: ')

    if operador_number == 1:
        operador = '+'
        resultado = numero_1 + numero_2
    elif operador_number == 2:
        operador = '-'
        resultado = numero_1 - numero_2
    elif operador_number == 3:
        operador = '*'
        resultado = numero_1 * numero_2
    else:  # 4
        operador = '/'
        if numero_2 == 0:
            print('Erro: divisão por zero. Tente novamente.')
            continue
        resultado = numero_1 / numero_2

    print(f'Operador selecionado: {operador}')
    break

print(f'{numero_1} {operador} {numero_2} = {resultado}')
