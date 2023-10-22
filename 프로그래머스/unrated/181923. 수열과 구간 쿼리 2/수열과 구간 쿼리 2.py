def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        filtered = sorted([arr[i] for i in range(s, e+1) if arr[i] > k])

        if not filtered:
            answer.append(-1)
        else:
            answer.append(filtered[0])
    return answer
