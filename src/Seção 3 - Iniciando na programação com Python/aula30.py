velocidade = 61
local_carro = 98

RADAR_1 = 60
LOCAL_1 = 100
RANGER_RANGE = 1

# Verificar velocidade
acima_velocidade = velocidade > RADAR_1

# Definir range do radar
inicio_range = LOCAL_1 - RANGER_RANGE
fim_range = LOCAL_1 + RANGER_RANGE

# Verificar se está no range
range_multa = inicio_range <= local_carro <= fim_range

# Verificar se foi multado
carro_multado = acima_velocidade and range_multa

def texto(var: bool) -> str:
    return "Sim" if var else "Não"

print(f'Velocidade acima do limite? {texto(acima_velocidade)} - Velocidade: {velocidade}')
print(f'Carro no range do radar? {texto(range_multa)}')
print(f'Carro foi multado? {texto(carro_multado)}')

if carro_multado:
    print('O carro foi multado.')
elif not range_multa and not acima_velocidade:
    print('O motorista não estava no range do radar e estava abaixo da velocidade.')
elif not range_multa:
    print('O motorista não estava no range do radar, mas estava acima da velocidade.')
else:
    print('O motorista estava no range do radar, mas abaixo da velocidade limite.')
