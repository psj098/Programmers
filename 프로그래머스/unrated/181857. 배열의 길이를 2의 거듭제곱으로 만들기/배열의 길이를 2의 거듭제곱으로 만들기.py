def solution(arr):
    current_length = len(arr)
    power = 1
    while power < current_length:
        power *= 2

    zeros_to_add = power - current_length
    answer = arr + [0] * zeros_to_add
    return answer
