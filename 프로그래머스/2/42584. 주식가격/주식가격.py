def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for time, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            past, _ = stack.pop()
            answer[past] = time - past
            
        stack.append([time, price])
    
    for time, price in stack:
        answer[time] = len(prices) - 1 - time
    
    return answer