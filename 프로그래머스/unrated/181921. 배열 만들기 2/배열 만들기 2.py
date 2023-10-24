def solution(l, r):
    result = []
    
    for num in range(l, r+1):
        if set(str(num)) <= {"0", "5"}:  # "0"과 "5"로만 이루어진 경우
            result.append(num)
    
    if not result:  # 만약 결과가 없다면
        return [-1]
    
    return result
