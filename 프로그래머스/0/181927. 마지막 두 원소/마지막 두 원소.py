def solution(num):
    
    result = []
    
    for i in range(0, len(num)):
        result.append(num[i])
    
    if num[-1] > num[-2]:
        result.append(num[-1] - num[-2])
    else:
        result.append(num[-1]*2)
    return result