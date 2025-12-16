'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (A-F; 0-9)
'''

nome = 'Weslley'
preco = 1000.95897643
number = 1000
variavel = '%s, o preço é R$ %.2f' %(nome,preco)
print(variavel)

print('O hexadecimal de %d é %08X' %(number, number))
