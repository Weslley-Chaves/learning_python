'''
Docstring for Seção 3 - Iniciando na programação com Python.aula29

Introdução ao try/except
try - tentar executar o código
except - ocorreu algum erro ao tentar executar
'''

try:
    print(123)
    print(456)
    int('a')

except ValueError:
    print(ValueError)
