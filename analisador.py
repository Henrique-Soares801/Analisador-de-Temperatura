print("--- Análise de Temperatura Anual  ---")

# Variáveis para acumular a soma e contar os meses
soma_temperaturas = 0.0
total_meses = 12

print("Digite a temperatura média (em ºC) de cada mês do ano:")

# Loop para ler e somar as temperaturas dos 12 meses
for mes_num in range(1, total_meses + 1):
    temp = float(input(f"Temperatura do mês {mes_num}: "))
    soma_temperaturas += temp

# Calcula a média anual
media_anual = soma_temperaturas / total_meses

print("\n" + "="*30)
print(f"🌡️ Média anual calculada: {media_anual:.2f} ºC")
print("="*30 + "\n")
