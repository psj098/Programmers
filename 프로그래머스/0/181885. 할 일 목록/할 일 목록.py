def solution(todo_list, finished):
    result = [] 
    for i, condition in enumerate(finished): 
        if condition == False: 
            result.append(todo_list[i])
    return result 