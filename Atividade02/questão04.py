# Atividade Prática 04 - Calculadora de Consumo de Combustível

# Entrada de dados pelo usuário
distancia = float(input("Digite a distância percorrida (km): "))
combustivel = float(input("Digite o combustível gasto (litros): "))

# Cálculo do consumo médio (km/l)
consumo_medio = distancia / combustivel

# Exibição dos resultados formatados
print("\n--- Relatório da Viagem ---")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {combustivel:.2f} litros")
print(f"Consumo médio se for um fiat12: {consumo_medio:.2f} km/l")
