import math 

def solution(slice, n):
    pizzas_needed = math.ceil(n / slice) 
    return pizzas_needed