def solution(n):
    
    result1 = 0
    result2 = 0
    
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                result1 += i**2
        return result1
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                result2 +=i
        return result2