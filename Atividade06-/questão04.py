import requests

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        # A chave no JSON é algo como "USDBRL" para USD-BRL
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        info = dados[chave]
        valor_atual = info.get("bid", "N/A")
        maxima = info.get("high", "N/A")
        minima = info.get("low", "N/A")
        atualizacao = info.get("create_date", "N/A")

        print(f"\nCotação {moeda}/BRL:")
        print(f"Valor atual: {valor_atual}")
        print(f"Máxima: {maxima}")
        print(f"Mínima: {minima}")
        print(f"Última atualização: {atualizacao}")

    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Exemplo de execução
consultar_moeda("USD")  # Consulta Dólar em relação ao Real
