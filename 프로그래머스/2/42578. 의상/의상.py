def solution(clothes):
    memo = {}
    
    for cloth, type in clothes:
        memo[type] = memo.get(type, 1) + 1
    
    answer = 1
    
    for key in memo:
        answer *= memo[key]
    
    return answer - 1