import string
import unicodedata

def limpar_texto(texto: str) -> str:
    """
    Remove espaços, pontuação e acentos do texto.
    """
    # Coloca em minúsculo
    texto = texto.lower()

    # Remove acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # Remove espaços e pontuação
    texto = ''.join(ch for ch in texto if ch not in string.punctuation and ch != ' ')

    return texto

def eh_palindromo(texto: str) -> str:
    """
    Verifica se o texto é palíndromo.
    Retorna "Sim" ou "Não".
    """
    texto_limpo = limpar_texto(texto)
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Programa principal
print("=== Verificador de Palíndromo ===")

frase = input("Digite uma palavra ou frase: ")

resultado = eh_palindromo(frase)

print(f"\nA frase '{frase}' é palíndromo? {resultado}")
