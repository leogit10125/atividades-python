# Calculadora de Descontos

# Entrada de dados 
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# Cálculo do valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# preço final com desconto
preco_final = preco_original - valor_desconto

# resultados 
print("\n--- Detalhes da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
