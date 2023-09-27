def solution(str1, str2): 
    if len(str1) != len(str2): 
        raise ValueError("Both strings should have the same length")
        
    answer = [] 
    
    for i in range(len(str1)): 
        answer.append(str1[i]) 
        answer.append(str2[i]) 
    
    return ''.join(answer) 