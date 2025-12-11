# Aprendendo a utilizar a função inpút para coletar dados

# Observação: funciona apenas no terminal - a função só finaliza a execução depois da interação do usuário

nome = input('Qual o seu nome? ') # input sem coerção sempre vai retornar str
idade = input('Qual sua idade? ') # input sem coerção sempre vai retornar str
altura = float(input('Qual a sua altura em metros? ').replace(',', '.')) # O melhor jeito é receber o valor como str - checar e só depois colocar ele em uma nova váriavel fazendo a conversão

print(f'{nome = }')
print(f'{idade = }')
print(f'{altura = }')

print(type(nome))
print(type(idade))
print(type(altura))
