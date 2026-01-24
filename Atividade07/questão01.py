import csv

def salvar_csv(nome_arquivo, dados):
    try:
        # Abre o arquivo no modo escrita
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)

            # Cabeçalho
            escritor.writerow(["Nome", "Idade", "Cidade"])

            # Dados em formato tabular
            for pessoa in dados:
                escritor.writerow(pessoa)

        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

# Exemplo de dados
pessoas = [
    ["maria", 25, "São Paulo"],
    ["carla", 30, "Rio de Janeiro"],
    ["marineide ventura", 22, "Salvador"],
    ["leone gomes", 44, "Itagi bahia"]
]

# Solicita ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
salvar_csv(nome_arquivo, pessoas)
