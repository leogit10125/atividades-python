# Atividade Prática 02 - Conversor de Moeda

# Entrada de dados pelo usuário
valor_reais = float(input("Digite o valor em reais (R$): "))
taxa_dolar = float(input("Digite a taxa do dólar (R$): "))
taxa_euro = float(input("Digite a taxa do euro (R$): "))

# Cálculos de conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Saída, duas casas decimais
print(f"\nValor em reais: R$ {valor_reais:.2f}")
print(f"Convertido para dólares: US$ {valor_dolar:.2f}")
print(f"Convertido para euros: € {valor_euro:.2f}")
