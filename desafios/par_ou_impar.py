def number(prompt):
    while True:
        entrada = input(prompt)
        try:
            return int(entrada)
        except ValueError:
            print('O valor digitado não é um número. [TENTE NOVAMENTE]')

def par_ou_impar(numero):
    return 'par' if numero % 2 == 0 else 'ímpar'

numero = number('Digite um número: ')
print(f'{numero} é {par_ou_impar(numero)}.')
