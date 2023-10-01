def solution(a, b):
    
    product_1 = int(str(a) + str(b)) 
    product_2 = 2 * a * b 
    answer = max(product_1, product_2) 
    
    return answer