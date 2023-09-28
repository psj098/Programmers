def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning)) 
    
    result = [] 
    for name_list in photo: 
        sum = 0 
        for person in name_list: 
            if person in score_dict: 
                sum += score_dict[person] 
        result.append(sum) 
    
    return result