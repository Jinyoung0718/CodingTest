def solution(num):
    result = ""
    
    for i in range(1, len(num)):
        temp = num[i] - num[i-1]
        
        if temp == 1:
            result += "w"
        elif temp == -1:
            result += "s"
        elif temp == 10:
            result += "d"
        elif temp == -10:
            result += "a"
            
    return result
            
    