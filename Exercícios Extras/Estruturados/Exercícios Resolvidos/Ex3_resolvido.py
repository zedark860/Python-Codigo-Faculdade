
def sequencia_collatz(n:int) -> list:
    if n < 0:
        raise ValueError("O numero inicial deve ser um inteiro positivo")

    sequencia:list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n //2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

numero:int = 6
print(sequencia_collatz(numero))