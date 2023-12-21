def solution(arr, k):
    unique_numbers = []
    for num in arr:
        if num not in unique_numbers:
            unique_numbers.append(num)
        if len(unique_numbers) == k:
            break
    while len(unique_numbers) < k:
        unique_numbers.append(-1)
    return unique_numbers