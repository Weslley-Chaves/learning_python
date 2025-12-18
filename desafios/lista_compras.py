import os

lista = []

def listar(lista):
    if not lista:
        print('Itens na lista: (vazia)')
        return
    print('Itens na lista:')
    for i, item in enumerate(lista, start=1):
        print(f'- {item}')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print('\nLISTA DE COMPRAS')
    print('Adicione um item na lista. Se quiser parar de adicionar digite [FIM]\n')

while True:
    try:
        header()
        item_bruto = input('Qual item você deseja adicionar a lista? ').strip()

        if item_bruto.upper() == 'FIM':
            limpar_terminal()
            print('Programa Encerrado\n')

            if lista:
                print('LISTA SEM ORDENAÇÃO\n')
                listar(lista)

                print('\nLISTA COM ORDENAÇÃO\n')
                listar(sorted(lista))
            else:
                print('Lista vazia.')

            break

        if not item_bruto:
            limpar_terminal()
            print('Você não digitou um item. Tente novamente.')
            continue

        item = item_bruto.capitalize()

        if item not in lista:
            lista.append(item)
            limpar_terminal()
            listar(lista)
        else:
            limpar_terminal()
            listar(lista)
            print(f'\n{item} já está na lista. Tente adicionar outro item.')
    except KeyboardInterrupt:
        limpar_terminal()
        print('\nPrograma encerrado pelo usuário.')
        break
