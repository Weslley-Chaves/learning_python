'''
#Precedência dos operadores aritméticos em Python:

1. (n + n)
2. **
3. * / // %
4. + -
'''
# Resultado esperado: 1024

# Exemplos:
conta_1 = 1 + 1 ** 5 + 5 # Incorreta
print(conta_1) # Resultado = 7

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2) # Resultado = 1024
