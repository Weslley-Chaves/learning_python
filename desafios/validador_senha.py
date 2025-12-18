tam_min_caracteres = 8

while True:
    try:
        senha = input('Digite uma senha: ').strip()

        if not senha:
            print('Você não digitou nada. [TENTE NOVAMENTE]')
            continue

        if len(senha) < tam_min_caracteres:
            print(f'A senha deve ter no mínimo {tam_min_caracteres} caracteres.')
            continue

        # any é utilizada para verificar a existência de algo dentro de um iterável
        # any(condição for elemento in iterável)
        tem_numero = any(c.isdigit() for c in senha) # Para cada 'caracter' em senha, verifique a condição
        tem_letra = any(c.isalpha() for c in senha)

        if tem_numero and tem_letra:
            print('A senha digitada é válida.')
            break
        else:
            print('A senha digitada é inválida.')
            if not tem_letra:
                print('Você deve ter no mínimo uma letra. [TENTE NOVAMENTE]')
            if not tem_numero:
                print('Você deve ter no mínimo um número. [TENTE NOVAMENTE]')

    except KeyboardInterrupt:
        print('\nPrograma encerrado pelo usuário.')
        break
