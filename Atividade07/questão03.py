import json

def salvar_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("\nDados lidos do arquivo:")
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Cidade: {dados['cidade']}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Solicita ao usuário os dados da pessoa
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cidade = input("Digite a cidade: ")

# Cria o dicionário com os dados informados
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

# Solicita ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

# Salva os dados no arquivo
salvar_json(nome_arquivo, pessoa)

# Lê os dados do arquivo
ler_json(nome_arquivo)
