def solution(clothes):
    
    memo = {}
    answer = 1
    
    for _, kind in clothes:
        memo[kind] = memo.get(kind, 0) + 1
    
    for value in memo.values():
        answer *= (value + 1)
    
    return answer - 1