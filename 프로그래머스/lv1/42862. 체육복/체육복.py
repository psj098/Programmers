def solution(n, lost, reserve): 
    # Intersection of lost and reserve
    intersection = set(lost) & set(reserve) 
    
    # Remove intersection students from both lists 
    lost = list(set(lost) - intersection) 
    reserve = list(set(reserve) - intersection)
    
    borrowed = 0 
    for r in reserve: 
        if r-1 in lost: 
            lost.remove(r-1) 
            borrowed += 1 
        elif r+1 in lost: 
            lost.remove(r+1) 
            borrowed += 1 
    
    answer = n - len(lost) 
    
    return answer 