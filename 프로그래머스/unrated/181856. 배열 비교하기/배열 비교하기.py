def solution(arr1, arr2):
    if len(arr1) != len(arr2): 
        return -1 if len(arr1) < len(arr2) else 1 
    
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    if sum_arr1 != sum_arr2:
        return -1 if sum_arr1 < sum_arr2 else 1

    return 0 




