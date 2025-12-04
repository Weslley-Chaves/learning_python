# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

# O mesmos operador pode fazer coisas diferentes - Polimorfismo
print(1+1) # Somar
print('a'+'b') # Concatenar
# print('a'+ 1)  Gera um erro; não é possível unir dois tipos sem convertê-los antes


print('1', type('1'), sep=" = ")
print(int('1')+1, type(int('1')+1),sep=" = ") # Realizando a coerção de tipo str -> int

print(bool(1 == 2), type(bool(1 == 2)), sep=" = ")

print('Weslley é da turma',str(11)+'A.')
