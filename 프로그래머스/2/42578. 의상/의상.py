def solution(clothes):
    
    memo = {}
    answer = 1
    
    for cloth, kind in clothes:
        memo[kind] = memo.get(kind, 0) + 1
    
    for key in memo.keys():
        answer *= (memo[key] + 1)
    
    return answer - 1