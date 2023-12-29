def solution(n_str):
    for n, alpha in enumerate(n_str): 
        if alpha != '0': 
            return n_str[n:]