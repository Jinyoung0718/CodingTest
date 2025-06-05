def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for idx, val in enumerate(prices):
        if stack:
            while stack != [] and stack[-1][1] > val:
                past, _ = stack.pop()
                answer[past] = idx - past
                
        stack.append([idx, val])
    
    for idx, val in stack:
        answer[idx] = len(prices) - 1 -idx
    
    return answer