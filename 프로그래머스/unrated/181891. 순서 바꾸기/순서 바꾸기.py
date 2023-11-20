def solution(num_list, n):
    initial_list = num_list[n:]
    subsequent_list = num_list[:n] 
    final_list = initial_list + subsequent_list 
    return final_list 
    