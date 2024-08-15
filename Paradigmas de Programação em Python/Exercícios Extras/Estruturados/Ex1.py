#Escreva uma função que receba dois termos iniciais e devolva uma lista com 10 inteiros da sequência Fibonacci;

termo1: int = 1
termo2: int = 0

def fibonacciSequence(termo1, termo2) -> list:
    lista_dez_termos = list()
    
    for _ in range(10):
        soma: int = termo1 + termo2
        termo1 = termo2
        termo2 = soma
        lista_dez_termos.append(soma)

    return lista_dez_termos

resultado = fibonacciSequence(termo1=termo1, termo2=termo2)

print(resultado)