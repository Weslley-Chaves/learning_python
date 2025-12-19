"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
print('''Verifique o tamanho do seu nome

    Condição    |    Descrição
----------------------------------
      <=  4     |      Curto
      5 - 6     |      Normal
      >=  7     |      Grande

''')

nome = input('Digite o seu primeiro nome: ').strip()

if not nome:
    print('Você não digitou um nome válido.')
else:
    tamanho_nome = len(nome)

    if tamanho_nome <= 4:
        print(f'Seu nome tem {tamanho_nome} letras e é considerado um nome CURTO.')
    elif 5 <= tamanho_nome <= 6:
        print(f'Seu nome tem {tamanho_nome} letras e é considerado um nome NORMAL.')
    else:
        print(f'Seu nome tem {tamanho_nome} letras e é considerado um nome GRANDE.')
