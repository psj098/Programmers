def solution(n, k):
    solution = [] 
    for num in range(k, n+1, k): 
        solution.append(num) 
    return solution