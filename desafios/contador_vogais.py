"""
8) Contador de Vogais

Dado um texto, conte quantas vogais ele contém.

Diferencie vogais maiúsculas e minúsculas (ou simplesmente normalize para minúsculas).

Mostre uma tabela simples no terminal: A: 3, E: 5, etc.

Foco de aprendizado: dicionários para contagem, loops.
"""

print('CONTADOR DE VOGAIS\n')
texto = input('Digite qualquer texto: ').lower()

vogais = [{'vogal': 'a', 'quantidade': 0},
          {'vogal': 'e', 'quantidade': 0},
          {'vogal': 'i', 'quantidade': 0},
          {'vogal': 'o', 'quantidade': 0},
          {'vogal': 'u', 'quantidade': 0}]

for letra in texto:
        for item in vogais:
            if item['vogal'] == letra:
                item['quantidade'] += 1

print('\nRESULTADO:\n')
for i in vogais:
    print(f"{i['vogal'].upper():>10} - {i['quantidade']}")

