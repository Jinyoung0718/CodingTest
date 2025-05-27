def solution(arr):
    stack = []
    
    for num in arr:
        if stack and num == stack[-1]:
            continue
        else:
            stack.append(num)
    
    return stack