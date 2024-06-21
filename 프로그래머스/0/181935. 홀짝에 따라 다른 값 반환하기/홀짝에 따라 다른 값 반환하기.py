def solution(n):
    
    result = 0
    
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                result += i**2
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                result += i
    return result
                
            
        
                