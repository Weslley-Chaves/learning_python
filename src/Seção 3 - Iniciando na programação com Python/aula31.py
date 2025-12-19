'''
Docstring for Seção 3 - Iniciando na programação com Python.aula31

flags (bandeiras) - marcando um local
none = Não valor

is e is not = é ou não é (tipo, valor, identidade)
'''

x = 'exemplo'
y = 'exemplo'

# Possuem o mesmo valor na memória
print(id(x))
print(id(y))

flag = None
condicao = True

if condicao:
    flag = True
    print('Passou no IF')
else:
    print('Passou no ELSE')

print(flag is None)
print(flag is not None)
