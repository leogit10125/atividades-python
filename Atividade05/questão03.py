def calcular_desconto(preco: float, porcentagem: float) -> float:
    """
    Calcula o valor do desconto com base no preço e na porcentagem.
    """
    return preco * (porcentagem / 100)


def preco_final(preco: float, porcentagem: float) -> float:
    """
    Retorna o preço final após aplicar o desconto.
    """
    desconto = calcular_desconto(preco, porcentagem)
    return preco - desconto


# Programa principal
print("=== Calculadora de Desconto ===")

try:
    # Entrada do usuário
    preco = float(input("Digite o preço do produto (R$): "))
    porcentagem = float(input("Digite a porcentagem de desconto (%): "))

    # Cálculos
    desconto = calcular_desconto(preco, porcentagem)
    final = preco_final(preco, porcentagem)

    # Saída formatada
    print(f"\nPreço original: R$ {preco:.2f}")
    print(f"Desconto aplicado: {porcentagem:.1f}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Preço final com desconto: R$ {final:.2f}")

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números.")
