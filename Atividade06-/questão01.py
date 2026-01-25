import random
import string

def gerar_senha(tamanho, caracteres):
    # Gera a senha aleatória com base nos caracteres escolhidos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    
    # Pergunta se o usuário quer definir os caracteres
    escolha = input("Deseja escolher os caracteres da senha? (s/n): ").lower()
    
    if escolha == 's':
        caracteres = input("Digite os caracteres que deseja usar: ")
        if not caracteres:
            print("⚠️ Você não digitou nenhum caractere. Usando padrão (letras, números e símbolos).")
            caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        # Conjunto padrão: letras, números e símbolos
        caracteres = string.ascii_letters + string.digits + string.punctuation
    
    if tamanho < 4:
        print("⚠️ Para maior segurança, escolha pelo menos 4 caracteres.")
    else:
        senha = gerar_senha(tamanho, caracteres)
        print(f"Sua senha segura é: {senha}")

except ValueError:
    print("Por favor, insira um número válido.")
