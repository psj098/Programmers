def solution(myString):
    chars = list(myString)

    for i in range(len(chars)):
        if chars[i] < 'l':
            chars[i] = 'l'

    return ''.join(chars)

