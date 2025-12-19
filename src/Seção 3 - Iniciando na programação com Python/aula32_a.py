"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def verificar_num_inteiro(prompt: str) -> int:
    while True:
        entrada = input(prompt).strip()
        try:
            return int(entrada)
        except ValueError:
            print('Você não digitou um número inteiro. Tente novamente!')


def par_impar(numero: int) -> str:
    return "Par" if numero % 2 == 0 else "Ímpar"


numero = verificar_num_inteiro('Digite um número inteiro: ')
print(f'O número {numero} é {par_impar(numero)}.')
