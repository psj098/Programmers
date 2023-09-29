def solution(a, b):
    result_1 = int(str(a) + str(b)) 
    result_2 = int(str(b) + str(a)) 
    answer = max(result_1, result_2) 
    
    return answer