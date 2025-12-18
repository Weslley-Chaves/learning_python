import os
import time

def main():
    while True:
        print('CONTADOR DE NÚMEROS PRESENTES EM UM TEXTO\n')

        entrada = input('Digite qualquer coisa: ')

        if not entrada.strip():
            print('Você não digitou nada. [TENTE NOVAMENTE]')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        digitos_validos = []
        digitos_invalidos = []

        for i in entrada:
            if i.isdigit():
                digitos_validos.append(i)
            else:
                digitos_invalidos.append(i)

        print(f'''“{entrada}” → {len(digitos_validos)} dígitos válidos | {len(digitos_invalidos)} dígitos inválidos.

Os dígitos válidos são: {digitos_validos}

Os dígitos inválidos são: {digitos_invalidos}''')
        break

main()
