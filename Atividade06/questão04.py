from datetime import datetime

print("=== Calculadora de Dias de Vida ===")

try:
    # Entrada do usuário
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    # Converter para objeto datetime
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    # Data atual
    hoje = datetime.today()

    # Diferença em dias
    dias_vivo = (hoje - nascimento).days

    # Saída
    print(f"\nVocê está vivo há {dias_vivo} dias.")

except ValueError:
    print("Formato inválido! Digite a data no formato dd/mm/aaaa.")
