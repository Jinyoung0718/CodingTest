def solution(number, k):
    
    answer = ""
    stack = []
    
    for num in number:
        
        while k > 0 and stack and stack[-1] < num:
            k -= 1
            stack.pop()
        
        stack.append(num)
    
    for n in stack:
        answer += n
    
    return answer[:len(number) - k]