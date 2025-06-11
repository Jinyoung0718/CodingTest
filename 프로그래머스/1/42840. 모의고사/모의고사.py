def solution(answers):
    answer = [0] * 3
    result = []
    
    a = [1, 2, 3, 4, 5] * 10000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    memo_a = {}
    memo_b = {}
    memo_c = {}
    
    for i in range(10000):
        memo_a[i] = a[i]
        memo_b[i] = b[i]
        memo_c[i] = c[i]
    
    for idx, val in enumerate(answers):
        if memo_a[idx] == val:
            answer[0] += 1
        if memo_b[idx] == val:
            answer[1] += 1
        if memo_c[idx] == val:
            answer[2] += 1

    max_score = max(answer)

    for idx, score in enumerate(answer):
        if score == max_score:
            result.append(idx + 1)

    return result

