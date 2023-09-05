def selection_sort(arr: list[int]) -> list[int]:
    lst = arr[:]

    if len(lst) <= 1:
        return lst
    
    for i in range(len(lst)):
        max_idx = i
        
        for j in range(i + 1, len(lst)):
            if lst[max_idx] < lst[j]:
                max_idx = j
        
        
        lst[i], lst[max_idx] = lst[max_idx], lst[i]

    return lst
    