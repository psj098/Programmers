def solution(intStrs, k, s, l):
    value_list = [] 
    for intstr in intStrs: 
        value = int(intstr[s:s+l])
        if value > k: 
            value_list.append(value) 
    return value_list