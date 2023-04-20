import json

# Ler o arquivo JSON com os dados de faturamento diário
with open('faturamento.json', 'r') as f:
    dados_faturamento = json.load(f)

# Inicializar as variáveis para o menor e maior valor de faturamento
menor_faturamento = float('inf')
maior_faturamento = float('-inf')

# Inicializar a variável para a soma do faturamento
soma_faturamento = 0

# Inicializar a variável para contar os dias com faturamento acima da média
dias_acima_da_media = 0

# Calcular o menor e maior valor de faturamento e a soma do faturamento
for faturamento_diario in dados_faturamento:
    if faturamento_diario > maior_faturamento:
        maior_faturamento = faturamento_diario
    if faturamento_diario < menor_faturamento:
        menor_faturamento = faturamento_diario
    soma_faturamento += faturamento_diario

# Calcular a média mensal, ignorando os dias sem faturamento
dias_com_faturamento = len([f for f in dados_faturamento if f > 0])
media_faturamento = soma_faturamento / dias_com_faturamento

# Contar o número de dias em que o valor de faturamento diário foi superior à média mensal
for faturamento_diario in dados_faturamento:
    if faturamento_diario > media_faturamento:
        dias_acima_da_media += 1

# Imprimir os resultados
print('Menor faturamento diário:', menor_faturamento)
print('Maior faturamento diário:', maior_faturamento)
print('Número de dias com faturamento acima da média:', dias_acima_da_media)