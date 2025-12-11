def entry_number(prompt):
    while True:
        number = input(prompt)
        try:
            entry = int(number)
            return entry
        except ValueError:
            print(f'O valor {number} não é válido. Tente novamente')
            continue

primeiro_valor = entry_number('Digite um valor: ')
segundo_valor = entry_number('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
else:
    print('O valores digitados são iguais')
