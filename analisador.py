print("--- Análise de Temperatura Anual  ---")  
  
# Variáveis para acumular a soma e contar os meses  
soma_temperaturas = 0.0  
total_meses = 12  
  
print("Digite a temperatura média (em ºC) de cada mês do ano:")  
  
# Primeiro loop: apenas para somar e calcular a média  
for mes_num in range(1, total_meses + 1):  
    temp = float(input(f"Temperatura do mês {mes_num}: "))  
    soma_temperaturas += temp  
  
# Calcula a média anual  
media_anual = soma_temperaturas / total_meses  
  
print("\n" + "="*30)  
print(f"🌡️ Média anual calculada: {media_anual:.2f} ºC")  
print("="*30 + "\n")  
  
print("Para descobrir quais meses ficaram acima da média sem usar listas,")  
print("o programa precisaria pedir os dados novamente ou usar 12 variáveis.")  
print("Alternativa: Defina uma temperatura meta para comparar os próximos dados!")