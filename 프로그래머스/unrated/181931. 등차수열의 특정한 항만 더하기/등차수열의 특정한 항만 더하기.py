def solution(a, d, included):
    answer = 0 
    
    for idx, cond in enumerate(included): 
        if cond: 
            answer += (a + idx * d)
    
    return answer