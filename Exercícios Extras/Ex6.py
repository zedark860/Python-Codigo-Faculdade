# Escreva um algoritmo que receba uma cadeia de caracteres e faça um histograma das letras;

histograma = {}

def criar_histograma(cadeia_caracteres):
    for letra in cadeia_caracteres:
        if letra in histograma.keys():
            histograma[letra] += 1
        else:
            histograma[letra] = 1
    return histograma

resultado = criar_histograma("aaewkasbb")
print(resultado)