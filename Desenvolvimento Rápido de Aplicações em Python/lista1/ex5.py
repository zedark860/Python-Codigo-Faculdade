def avg_list_numbers(number_list: list, total_numbers: int, sum_numbers: int = 0) -> int:
    if len(number_list) == 1:
        return (sum_numbers + number_list[0]) / total_numbers
    
    sum_numbers += number_list[0]
    return avg_list_numbers(number_list[1:], total_numbers, sum_numbers)

number_list: list = [1, 2, 3, 4, 5]

total_numbers: int = len(number_list)

print(avg_list_numbers(number_list, total_numbers=total_numbers))