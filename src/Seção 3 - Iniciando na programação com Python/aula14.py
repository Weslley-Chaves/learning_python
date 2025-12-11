# Formatação de Strings com o método format

a = 'A'
b = 'B'
c = 1.1
formato = 'a={nome1} b={nome2} c={nome3:.2f} d={nome3}'.format(nome1=a, nome2=b, nome3=c) # Podemos criar parâmetros - ao criar um parâmetro, todos em frente a ele precisam também ser nomeados
# A formatação deve ser declarada dentro da frase
print(formato)


# Exemplo de como utilizar o método format:

nome = 'Weslley'
sobrenome = 'Santos Chaves'
idade = 24
altura = 1.81

frase = 'Meu nome é {0} {1}, tenho {2} anos e {3} de altura.'.format(nome, sobrenome, idade, altura) # Podemos também utilizar argumentos

print(frase)
