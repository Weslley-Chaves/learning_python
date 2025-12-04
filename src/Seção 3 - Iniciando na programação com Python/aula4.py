# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
print("Números inteiros:\n")
print(11) # int
print(-11) # int
print(0) # int


# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print("\nNúmeros com ponto flutuante:\n")
print(1.1, 10.5, sep="\n")
print(0.0)

# Tudo em Python é um objeto
# A função type mostra o tipo que o Python
# inferiu ao valor.
print("\nO tipo do objeto selecionado:\n")

print(type("Weslley"), "Weslley", sep=" Objeto selecionado: ")

print(type(11), 11, sep=" Objeto selecionado: ")

print(type(0.0), 0.0, sep=" Objeto selecionado: ")

print(type(True), True, sep=" Objeto selecionado: ")

print(type([]), [], sep=" Objeto selecionado: ")

print(type(()), (), sep=" Objeto selecionado: ")

print(type(dict()), dict(nome="Weslley", sobrenome="Chaves"), sep=" Objeto selecionado: ")

