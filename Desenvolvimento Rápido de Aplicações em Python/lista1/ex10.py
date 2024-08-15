def search_binary(number_list: list[int], target: int) -> int:
    low: int = 0
    high: int = len(number_list) - 1
    
    while low <= high:
        middle: int = (low + high) // 2
        if (number_list[middle] == target):
            return middle
        if (number_list[middle] > target):
            high = middle - 1
        else:
            low = middle + 1
    
    return -1

number_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(search_binary(number_list, 8)) # => 7
print(search_binary(number_list, 10)) # => -1