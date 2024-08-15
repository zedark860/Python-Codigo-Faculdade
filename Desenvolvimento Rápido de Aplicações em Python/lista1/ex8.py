def findSmallest(arr: list) -> int:
    
    smallest: int = arr[0]
    
    smallest_index: int = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index

def selection_sort(arr: list) -> list:
    new_arr: list = []
    
    for i in range(len(arr)):
        smallest: int = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
        
    return new_arr


arr: list = [5, 3, 6, 2, 10]

print(selection_sort(arr))