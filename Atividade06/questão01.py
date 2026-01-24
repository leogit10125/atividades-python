import csv

# Lista de listas com dados fictícios
dados_pessoas = [
    ["Nome", "Idade", "Cidade"],  # Cabeçalhos
    ["Ana Silva", 28, "São Paulo"],
    ["Carlos Souza", 35, "Rio de Janeiro"],
    ["Mariana Costa", 22, "Salvador"]
]

try:
    # Solicitando nome do arquivo CSV
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

    # Abre o arquivo para escrita
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)

        # Escreve os dados linha por linha
        for linha in dados_pessoas:
            escritor.writerow(linha)

    # Confirma a gravação
    print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'!")

except Exception as e:
    print(f"Ocorreu um erro ao gravar o arquivo: {e}")
