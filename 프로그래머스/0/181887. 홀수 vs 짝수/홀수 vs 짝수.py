def solution(num):
    
    a = 0
    b = 0
    
    for i in range (len(num)):
        if i % 2 == 0:
            a += num[i]
        else:
            b += num[i]
    
    return a if a > b else b