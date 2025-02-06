def solution(arr):
    stack = []
    
    for n in arr:
        if stack and stack[-1] == n:
            continue
        stack.append(n)
    
    
    return stack