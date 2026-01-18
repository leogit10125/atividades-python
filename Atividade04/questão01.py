def calculadora():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis: +  -  *  /")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: digitar apenas números.")

# Executa a calculadora
calculadora()
