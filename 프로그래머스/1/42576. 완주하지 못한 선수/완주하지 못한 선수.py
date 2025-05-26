def solution(part, comp):
    memo = {}
    answer = 0
    
    for p in part:
        memo[p] = memo.get(p, 0) + 1
    
    for c in comp:
        memo[c] -= 1
    
    for i in memo:
        if memo[i] == 1:
            answer = i
    
    return answer