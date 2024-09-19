import os

def limpar_terminal():
    os.system("cls")
    cabecalho()

def encerrar_programa():
    limpar_terminal()
    print("""
PROGRAMA ENCERRADO COM SUCESSO
""")
    exit()

def exibir_menu():
        
    print("""Deseja encerrar o programa? 
""")

    menu_opcoes = ['ENCERRAR O PROGRAMA','RETORNAR AO MENU ANTERIOR','LISTAR CATEGORIAS']

    for i, opcao in enumerate(menu_opcoes, start=1):

        print(f'DIGITE {[i]} PARA {opcao}.')
    
    resposta = verificar_input('')

    if resposta == 1:
        encerrar_programa()
    
    elif resposta == 2:
        main()
    elif resposta == 3:
        listar_categorias()
    else:
        print("""[Erro] O valor inserido não é VÁLIDO.
                    
TENTE NOVAMENTE""")

def listar_categorias():
    limpar_terminal()

    classificacao = ['MAGREZA','NORMAL','SOBREPESO','OBESIDADE GRAU 1','OBESIDADE GRAU 2','OBESIDADE GRAU 3']
    pontuacao = [0.00,18.5,25.00,30.00,35.00,40.00,...]

    formatacao = "+-------------------+-------------------+\n"
    formatacao += "|   Classificação   |     Pontuação     |\n"
    formatacao += "+-------------------+-------------------+\n"

    for i, (classif, pont) in enumerate(zip(classificacao, pontuacao), start=1):
        if i < len(pontuacao):
            if i < len(pontuacao) - 1:
                proximo_pont = pontuacao[i]
                formatacao += f"""| {classif:<18}| De {pont:>4} até {proximo_pont:<6}|
"""
            else:
                formatacao += f"""| {classif:<18}| De {pont} em diante.|
+-------------------+-------------------+
"""
    print(formatacao)
    exibir_menu()

def verificar_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            valor = float(user_input)
            if valor > 0:
                return(valor)
            else:
                limpar_terminal()
                print("""[Erro] O valor inserido não é VÁLIDO.
                                        
TENTE NOVAMENTE""")
                
        except ValueError:
            limpar_terminal()
            print("""[Erro] O valor inserido não é VÁLIDO.
                  
TENTE NOVAMENTE""")

def cabecalho():
    texto = "CALCULADORA DE IMC (Índice de Massa Corporal)"
    largura = len(texto) + 2
    print('+' + '-' * largura + '+')
    print(f"| {texto} |")
    print('+' + '-' * largura + '+')
    print("""
""")

def main():
    limpar_terminal()
    nome = input('Qual é o seu nome? ')
    limpar_terminal()

    print(f"""Olá, {nome}! Seja bem vindo a nossa aplicação para calcular o seu Índice de Massa Corporal (IMC).\n""")

    massa = verificar_input('Digite sua massa em Kg: ')
    altura = verificar_input('Digite sua altura em metros: ')

    limpar_terminal()

    dif = int(0)

    imc = int(massa / altura ** 2)  

    if altura == 1:
        p1 = f'{nome}, você possui {f'{altura:.2f}'.replace(".",",")} metro de altura, pesa {f'{massa:.0f}'.replace(".",",")} quilos e seu IMC está na pontuação {f'{imc:.1f}'.replace(".",",")}.\n'
    else:
        p1 = f'{nome}, você possui {f'{altura:.2f}'.replace(".",",")} metros de altura, pesa {f'{massa:.0f}'.replace(".",",")} quilos e seu IMC está na pontuação {f'{imc:.1f}'.replace(".",",")}.\n'

    if (imc < 18.5):
        print(p1)
        print("Você está abaixo do normal!")
        print ("CLASSIFICAÇÃO: MAGREZA")
        dif = 25 - imc
        print(f"""Faltam {dif} pontos para você atingir o peso ideal.
Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso, por isso, procure um especialista.""")
        
    if (imc >= 18.5) and (imc < 25):

        print(p1)
        print("Você está no peso ideal!")
        print("CLASSIFICAÇÃO: NORMAL")
        print("Permaneça assim, mantendo um estilo de vida ativo e uma alimentação equilibrada. PARABÉNS!")
        
    if (imc >= 25) and (imc < 30):
        print(p1)
        print("Você está um pouco acima do peso ideal!")
        print("CLASSIFICAÇÃO: SOBREPESO")
        dif = imc - 25
        print(f"""Faltam {dif} pontos para você atingir o peso ideal.
Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.""")

    if (imc >= 30) and (imc < 35):
        print(p1)
        print("Você NÃO está no peso ideal!")
        print("CLASSIFICAÇÃO: OBESIDADE GRAU I")
        dif = imc - 25
        print(f"""Faltam {dif} pontos para você atingir o peso ideal. 
O SOBREPESO é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.""")

    if (imc >= 35) and (imc < 40):
        print(p1)
        print("Você NÃO está no peso ideal!")
        print("CLASSIFICAÇÃO: OBESIDADE GRAU II")
        dif = imc - 25
        print(f"""Faltam {dif} pontos para você atingir o peso ideal.
Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.""")

    if (imc >= 40):
        print(p1)
        print("Você NÃO está no peso ideal!")
        print("CLASSIFICAÇÃO: OBESIDADE GRAU III")
        dif = imc - 25
        print(f"""Faltam {dif} pontos para você atingir o peso ideal.
Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.""")
    
    print("""
""")
    exibir_menu()
if __name__ == "__main__":
    main()