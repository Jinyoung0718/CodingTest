def solution(num):
    
    sum = 0
    temp = list(num)
    
    for i in temp:
        sum += int(i)
    
    return sum % 9