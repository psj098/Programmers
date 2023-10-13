def solution(a, b, c):
    sum_val = a + b + c
    sum_square = a**2 + b**2 + c**2
    sum_cube = a**3 + b**3 + c**3
    
    if a != b and a != c and b != c:
        return sum_val
    elif a == b and a == c:
        return sum_val * sum_square * sum_cube
    else:
        return sum_val * sum_square
