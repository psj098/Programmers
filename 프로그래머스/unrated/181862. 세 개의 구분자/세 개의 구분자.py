def solution(myStr):
    split_str = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()

    if not split_str:
        return ["EMPTY"]

    return split_str