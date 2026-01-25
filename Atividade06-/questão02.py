import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # lança erro se status != 200
        dados = resposta.json()
        
        usuario = dados["results"][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]
        
        print("Usuário encontrado:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Executa o programa
buscar_usuario()
