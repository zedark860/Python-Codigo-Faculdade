
def eh_palindromo() -> True:
    palavra:str = remover_espacos_e_conveter_minusculas(palavra)

    inicio = 0
    fim = len(palavra) - 1

    while inicio < fim:
        if palavra[inicio] != palavra[fim]:
            return False
        inicio += 1
        fim -= 1

    return True

def remover_espacos_e_conveter_minusculas(texto):
    novo_texto = ""
    for caracter in texto:
        
