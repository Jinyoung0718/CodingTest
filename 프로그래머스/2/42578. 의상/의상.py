def solution(clothes):
    memo = {}
    
    for cloth, type in clothes:
        memo[type] = memo.get(type, 1) + 1
    
    answer = 1
    
    for type in memo:
        answer *= memo[type]
    
    return answer - 1