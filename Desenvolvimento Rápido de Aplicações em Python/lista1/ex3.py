def multiplication_table(number: int) -> None:
    for i in range(1, 11):
        print(f'{number} x {i} = {number * i}')

number = int(input("Digite o valor para gerar a tabuada: "))

multiplication_table(number)