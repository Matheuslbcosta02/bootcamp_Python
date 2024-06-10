#comando for usado para percorrer um objeto iterável
#usamos quando sabemos quantas vezes vamos executar o bloco de código.

texto = input("digite uma palavra :")
VOGAIS = "AEIOU"

#pegar vogais de uma palavra
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")