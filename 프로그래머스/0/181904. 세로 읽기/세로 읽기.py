def solution(my_string, m, c):
    result = ''
    column = c - 1  

    for i in range(0, len(my_string), m):
        result += my_string[i + column]

    return result