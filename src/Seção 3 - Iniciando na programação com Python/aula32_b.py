def verificar_num_inteiro(prompt: str) -> int:
    while True:
        entrada = input(prompt).strip()
        try:
            return int(entrada)
        except ValueError:
            print('Você não digitou um número inteiro. Tente novamente!')


hora_atual = verificar_num_inteiro('Digite a hora atual (0–23): ')

if not 0 <= hora_atual <= 23:
    print(f'A hora {hora_atual} não é válida.')
elif 0 <= hora_atual <= 11:
    print(f'Bom dia! Agora são {hora_atual} horas.')
elif 12 <= hora_atual <= 17:
    print(f'Boa tarde! Agora são {hora_atual} horas.')
else:
    print(f'Boa noite! Agora são {hora_atual} horas.')
