import csv

try:
    # Solicita ao usuário o nome do arquivo CSV
    nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ")

    # Abre o arquivo para leitura
    with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)

        # Exibe cada linha como uma lista
        print("\nConteúdo do arquivo CSV:")
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
