def solution(part, comple):
    memo = {}
    
    for n in part:
        memo[n] = memo.get(n, 0) + 1
    
    for n in comple:
        memo[n] -= 1
    
    answer = [key for key, value in memo.items() if value == 1]
    return answer[0]