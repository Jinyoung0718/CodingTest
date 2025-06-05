def solution(participant, completion):
    
    memo = {}
    
    for part in participant:
        memo[part] = memo.get(part, 0) + 1
    
    for comp in completion:
        if comp in memo:
            memo[comp] -= 1
    
    return [key for key, val in memo.items() if val == 1][0]
