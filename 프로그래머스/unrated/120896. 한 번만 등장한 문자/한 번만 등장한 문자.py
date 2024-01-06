def solution(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    single_occurrence_chars = sorted([char for char, count in char_count.items() if count == 1])

    return ''.join(single_occurrence_chars)