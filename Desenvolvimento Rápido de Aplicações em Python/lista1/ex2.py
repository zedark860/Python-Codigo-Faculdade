def pair_or_impar(number: int) -> str:
    return 'par' if number % 2 == 0 else 'impar'

number: int = int(input("Digite o número para verificar se é impar ou par: "))

print(pair_or_impar(number))