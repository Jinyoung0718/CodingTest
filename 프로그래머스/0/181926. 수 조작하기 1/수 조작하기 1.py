def solution(n, control):
    
    sum = n
    
    c = {'w':1, 's':-1, 'd':10, 'a':-10}
    
    for i in control:
        sum += c[i]
        
    return sum