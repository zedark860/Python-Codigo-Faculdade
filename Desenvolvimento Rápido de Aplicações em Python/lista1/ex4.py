def recursion_max_number(number_list: list[int]) -> tuple[int, int]:
    if len(number_list) == 1:
        return number_list[0], number_list[0]
    
    min_value, max_value = recursion_max_number(number_list[1:])
    
    return min(number_list[0], min_value), max(number_list[0], max_value)

number_list: list[int] = []

for i in range(5):
    number: int = int(input("Digite um número: "))
    number_list.append(number)
num, num2 = recursion_max_number(number_list)

print(num, num2)