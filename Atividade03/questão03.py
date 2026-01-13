temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Primeiro, converter tudo para Celsius
if origem == "C":
    celsius = temperatura
elif origem == "F":
    celsius = (temperatura - 32) * 5 / 9
elif origem == "K":
    celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Depois, converter de Celsius para a unidade desejada
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9 / 5) + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"Temperatura convertida: {resultado:.2f}°{destino}")
