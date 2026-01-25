import requests

def consultar_cep():
    cep = input("Digite o CEP para consulta (somente números): ").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("\nInformações do CEP:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Executa o programa
consultar_cep()
