# Programa que analisa números e contar pares e ímpares

pares = 0
impares = 0

print("=== Analisador de Números ===")
print("Digite números inteiros. Para encerrar, digite 0.")

while True:
    try:
        numero = int(input("Digite um número: "))
        
        if numero == 0:  # condição de parada
            break
        
        if numero % 2 == 0:
            print(f"{numero} é PAR.")
            pares += 1
        else:
            print(f"{numero} é ÍMPAR.")
            impares += 1

    except ValueError:
        print("Erro: digite apenas números inteiros.")

print("\n=== Resultado Final ===")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
