def solution(nums):
    num_unique = len(set(nums)) 
    num_to_take = len(nums) // 2 
    result = min(num_unique, num_to_take) 
    
    return result