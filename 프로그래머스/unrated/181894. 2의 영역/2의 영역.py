def solution(arr):
    indices = [i for i, x in enumerate(arr) if x == 2]

    if not indices:
        return [-1]

    return arr[indices[0]:indices[-1] + 1]
