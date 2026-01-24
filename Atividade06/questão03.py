import json

#  dicionário com dados 
pessoa = {
    "nome": "leone gomes",
    "idade": 45,
    "cidade": "itagi bahia"
}

try:
    # Solicit nome do arquivo json
    nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

    # Salva os dados no arquivo jason
    with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo_json:
        json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

    print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'!")

    # Lê o arquivo
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo_json:
        dados_carregados = json.load(arquivo_json)

    # Exibe os dados 
    print("\nConteúdo do arquivo JSON:")
    print(dados_carregados)

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
