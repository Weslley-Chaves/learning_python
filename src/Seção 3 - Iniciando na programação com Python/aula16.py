# if, elif e else; se, se não se e se não

entrada = input('Você quer "entrar" ou "sair"? ').lower()

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu no sistema.')
else:
    print('Você não digitou um argumento válido ("entrar" ou "sair").')

print('FORA DO BLOCO CONDICIONAL')
