def number(prompt):
    while True:
        entrada = input(prompt)
        try:
            entrada = int(entrada)
            if entrada == 0:
                print('A idade não pode ser 0. [TENTE NOVAMENTE]')
            elif entrada >= 1:
                return entrada
            else:
                print('A idade não pode ser negativa. [TENTE NOVAMENTE]')
        except ValueError:
            print('Você não digitou um valor válido. [TENTE NOVAMENTE]')

def plural(qtd, singular, plural):
    return singular if qtd == 1 else plural

def entry(prompt):
    while True:
        entrada = input(prompt).strip()
        if entrada:
            return entrada
        print('Você não digitou um valor válido. [TENTE NOVAMENTE]')

nome = entry('Qual é o seu nome? ')
idade = number('Digite a sua idade: ')

nome_invertido = nome[::-1]
letra_inicial = nome[0]
letra_final = nome[-1]

qtd_espacos = nome.count(' ')
qtd_letras_nome = len(nome) - qtd_espacos

print(f"Seu nome é {nome}.")
print(f"Seu nome invertido é {nome_invertido}.")

if qtd_espacos > 0:
    palavra_espaco = plural(qtd_espacos, 'espaço', 'espaços')
    print(f"Seu nome tem {palavra_espaco}. Para ser mais exato, há {qtd_espacos} {palavra_espaco} em seu nome.")
else:
    print("Seu nome não tem espaços.")

print(f"Seu nome tem {qtd_letras_nome} {plural(qtd_letras_nome, 'letra', 'letras')}.")
print(f"A primeira letra do seu nome é {letra_inicial}.")
print(f"A última letra do seu nome é {letra_final}.")
