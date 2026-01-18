# Verificação de senha segura

senha = input("Digite sua senha: ")

# Critério A: pelo menos 8 caracteres
criterio_tamanho = len(senha) >= 8

# Critério B: conter pelo menos um número
criterio_numero = any(char.isdigit() for char in senha)

# Verificação final
if criterio_tamanho and criterio_numero:
    print("Senha válida! Atende aos critérios de segurança.")
else:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
