def solution(clothes):
    
    memo = {}
    answer = 1
    
    for cloth, kind in clothes:
        memo[kind] = memo.get(kind, 0) + 1
    
    
    for val in memo.values():
        answer *= (val + 1)
    
    return answer - 1