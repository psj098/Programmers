def solution(my_string, target):
    index = my_string.find(target)
    
    if index == -1:
        return 0
    else:
        return 1