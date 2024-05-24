
def criar_histograma(cadeia_caracteres:str) -> dict:
    histograma:dict = {}
    for letra in cadeia_caracteres:
        if letra.isalpha():
            letra = letra.lower()
            if letra in histograma.keys():
                histograma[letra] += 1
            else:
                histograma[letra] = 1
    return histograma

resultado = criar_histograma("aaewkasbb")
print(resultado)