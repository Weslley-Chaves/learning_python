import os # carrega uma biblioca interna que fornece funções para interagir com o sistema operacional

def limpar_terminal():
    os.system('cls') #cls é o comando para limpar o terminal no windowns

def encerrar_programa():
    limpar_terminal()
    print('PROGRAMA ENCERRADO.')
    exit() # encerra a execução do programa

def verificar_input(prompt): # o parametro prompt permite utilizar uma mensagem personilzada ao chamar a função
    while True:
        user_input = input(prompt)
        try: # conversão da entrada feita pelo usuário em type int - originalmente o input é caracterizado com type str
            return int(user_input)
        except ValueError: # VALUE_ERROR é a captura caso o usuário digite um valor que não possa ser convertido em int
            print("Erro: O input não é um número inteiro válido. Tente novamente.")

def retornar_menu():
    while True:
        print("""Digite [1] PARA RETORNAR AO MENU
Digite [2] PARA ENCERRAR O PROGRAMA
""")
        option = verificar_input("Escolha uma opção: ")
        if option == 1:
            limpar_terminal()
            return
        elif option == 2:
            encerrar_programa()
        else:
            limpar_terminal()
            print('Erro: Opção inválida. Tente novamente.')

def celsius_fahrenheit():
    limpar_terminal()
    while True:
        celsius = verificar_input('Digite a temperatura em Celsius: ')
        if celsius < -273.15:
            print("""Zero Absoluto (-273,15°C): Esse é o limite inferior teórico de temperatura.
Abaixo disso, não há mais energia térmica em um corpo, e as partículas estariam completamente imóveis (em teoria, pois nunca foi atingido na prática).
                  
[DIGITE OUTRO VALOR]""")
        else:
            resultado = (9/5 * celsius) + 32
            print(f"""A temperatura em Fahrenheit é {f"{resultado:.2f}".replace(".",",")}°F.
            """)
            retornar_menu()
            break

def celsius_kelvin():
    limpar_terminal()
    while True:
        celsius = verificar_input('Digite a temperatura em Celsius: ')

        if celsius < -273.15:
            print("""Zero Absoluto (-273,15°C): Esse é o limite inferior teórico de temperatura.
Abaixo disso, não há mais energia térmica em um corpo, e as partículas estariam completamente imóveis (em teoria, pois nunca foi atingido na prática).
                  
[DIGITE OUTRO VALOR]""")

        else:
            resultado = celsius + 273.15
            print(f"""A temperatura em Kelvin é {f"{resultado:.2f}".replace(".",",")} K.
            """)
            retornar_menu()
            break

def fahrenheit_celsius():
    limpar_terminal()
    while True:
        fahrenheit = verificar_input('Digite a temperatura em Fahrenheit: ')
        if fahrenheit < -459.67:
            print("""Zero Absoluto (-459,67°F): É o limite teórico inferior de temperatura, correspondente ao zero absoluto em Celsius.
                  
[DIGITE OUTRO VALOR]""")

        else:
            resultado = (fahrenheit - 32) * 5/9
            print(f"""A temperatura em Celsius é {f"{resultado:.2f}".replace(".",",")}°C.
            """)
            retornar_menu()
            break

def fahrenheit_kelvin():
    limpar_terminal()
    while True:
        fahrenheit = verificar_input('Digite a temperatura em Fahrenheit: ')
        if fahrenheit < -459.67:
            print("""Zero Absoluto (-459,67°F): É o limite teórico inferior de temperatura, correspondente ao zero absoluto em Celsius.
                  
[DIGITE OUTRO VALOR]""")

        else:
            resultado = (fahrenheit - 32) * 5/9 + 273.15
            print(f"""A temperatura em Kelvin é {f"{resultado:.2f}".replace(".",",")} K.
            """)
            retornar_menu()
            break

def kelvin_celsius():
    limpar_terminal()
    while True:
        kelvin = verificar_input('Digite a temperatura em Kelvin: ')
        if kelvin < 0:
            print("""Zero Absoluto (0 K): Este é o menor valor de temperatura possível no universo. Não existe valor negativo em Kelvin, pois a escala começa no zero absoluto.
                  
                                    
[DIGITE OUTRO VALOR]""")
        else:
            resultado = kelvin - 273.15
            print(f"""A temperatura em Celsius é {f"{resultado:.2f}".replace(".",",")}°C.
            """)
            retornar_menu()
            break

def kelvin_fahrenheit():
    limpar_terminal()
    while True:
        kelvin = verificar_input('Digite a temperatura em Kelvin: ')
        if kelvin < 0:
            print("""Zero Absoluto (0 K): Este é o menor valor de temperatura possível no universo. Não existe valor negativo em Kelvin, pois a escala começa no zero absoluto.
                  
                                    
[DIGITE OUTRO VALOR]""")
        else:
            resultado = (kelvin - 273.15) * 9/5 + 32
            print(f"""A temperatura em Fahrenheit é {f"{resultado:.2f}".replace(".",",")}°F.
            """)
            retornar_menu()
            break

def exibir_menu():

    texto_1 = 'Olá, seja bem-vindo ao nosso conversor de Escalas Termométricas!'
    largura = len(texto_1) + 2

    print('+' + '-' * largura + '+')
    print(f"| {texto_1} |")
    print('+' + '-' * largura + '+')

    menu_opcoes = ['CONVERSÃO DE CELSIUS PARA FAHRENHEIT',
                   'CONVERSÃO DE CELSIUS PARA KELVIN',
                   'CONVERSÃO DE FAHRENHEIT PARA CELSIUS',
                   'CONVERSÃO DE FAHRENHEIT PARA KELVIN',
                   'CONVERSÃO DE KELVIN PARA CELSIUS',
                   'CONVERSÃO DE KELVIN PARA FAHRENHEIT',
                   'ENCERRAR O PROGRAMA']

    for i, opcao in enumerate(menu_opcoes, start=1):
        print(f'DIGITE [{i}] PARA {opcao}')

def main():
    while True:
        exibir_menu()
        entrada = verificar_input("""
Escolha uma opção: """)
        
        if entrada == 1:
            celsius_fahrenheit()
        elif entrada == 2:
            celsius_kelvin()
        elif entrada == 3:
            fahrenheit_celsius()
        elif entrada == 4:
            fahrenheit_kelvin()
        elif entrada == 5:
            kelvin_celsius()
        elif entrada == 6:
            kelvin_fahrenheit()
        elif entrada == 7:
            encerrar_programa()
        else:
            limpar_terminal()
            print("Erro: O input não é um número válido. Tente novamente.")

if __name__ == "__main__":
    main()