def solution(part, comple):
    memo = {}
    
    for p in part:
        if p in memo:
            memo[p] += 1
            continue
        memo[p] = 1
    
    for c in comple:
        if c in memo:
            memo[c] -= 1
    
    return "".join(map(str, [key for key, value in memo.items() if value == 1]))