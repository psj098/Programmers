def solution(myString, pat):
    transformed_string = ''
    for char in myString:
        if char == 'A':
            transformed_string += 'B'
        else:
            transformed_string += 'A'

    return 1 if pat in transformed_string else 0