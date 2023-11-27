def solution(arr, intervals):
    result = [] 
    for interval in intervals: 
        result += arr[interval[0]: interval[1]+1]
    return result