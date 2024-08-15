def insertion_sort(number_list: list[int]) -> list[int]:
    for i in range(1, len(number_list)):
        j = i
        while j > 0 and number_list[j] < number_list[j - 1]:
            number_list[j], number_list[j - 1] = number_list[j - 1], number_list[j]
            j -= 1
    return number_list


number_list: list[int] = [5, 3, 6, 2, 10]

print(insertion_sort(number_list))