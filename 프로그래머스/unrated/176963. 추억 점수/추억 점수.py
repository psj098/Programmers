def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning)) 
    result = [sum(score_dict[person] for person in name_list if person in score_dict) for name_list in photo]

    return result 