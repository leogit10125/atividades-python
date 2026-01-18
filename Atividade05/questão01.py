def calcular_gorjeta(valor_conta: float, porcentagem: float) -> float:
    """
    Calcula o valor da gorjeta a ser deixada em um restaurante.
    """
    return valor_conta * (porcentagem / 100)


# Programa principal
print("=== Calculadora de Gorjeta ===")

try:
    # Entrada do usuário
    valor_conta = float(input("Digite o valor total da conta (R$): "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

    # Cálculo
    gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    total = valor_conta + gorjeta

    # Saída formatada
    print(f"\nValor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem:.1f}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números.")
