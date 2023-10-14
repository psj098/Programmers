def solution(num_list):
    
    odd_nums = [] 
    even_nums = [] 
    
    for num in num_list: 
        if num % 2 == 1: 
            odd_nums.append(str(num))
        else: 
            even_nums.append(str(num))
    
    odd_num = int(''.join(odd_nums)) if odd_nums else 0
    even_num = int(''.join(even_nums)) if even_nums else 0

    total_sum = odd_num + even_num 
    
    return total_sum
