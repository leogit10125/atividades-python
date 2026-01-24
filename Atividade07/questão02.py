import csv

def ler_csv(nome_arquivo):
    try:
        # Abre o arquivo no modo leitura
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)

            # Percorre cada linha e exibe na tela
            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Solicita ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo CSV para leitura: ")
ler_csv(nome_arquivo)
