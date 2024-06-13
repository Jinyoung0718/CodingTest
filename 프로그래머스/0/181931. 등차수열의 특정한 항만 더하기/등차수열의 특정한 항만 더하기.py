def solution(a, d, included):
    sum = 0
    
    for i, j in enumerate(included):
        if j == True:
            sum += (i*d) + a 
            
    return sum
        
        