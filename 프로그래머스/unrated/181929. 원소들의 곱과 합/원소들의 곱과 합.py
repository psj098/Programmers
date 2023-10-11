def solution(num_list):
    num_prod = 1
    num_sum = 0 
    
    for num in num_list: 
        num_prod *= num 
        num_sum += num 
        
    num_sum_sqrt = num_sum ** 2 

    return 1 if num_prod < num_sum_sqrt else 0 