def solution(arr, delete_list):
    result = [element for element in arr if element not in delete_list]
    return result