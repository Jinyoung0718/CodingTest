def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        if stack:
            while stack and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    
    for idx, _ in stack:
        answer[idx] = len(prices) - 1 - idx
    return answer