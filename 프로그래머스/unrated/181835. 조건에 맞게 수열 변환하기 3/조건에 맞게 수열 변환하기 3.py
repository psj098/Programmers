def solution(arr, k):
    if k % 2 == 0:
        transformed_arr = [x + k for x in arr]
    else:
        transformed_arr = [x * k for x in arr]
    return transformed_arr