def solution(sta, end):
    result = []
    
    for i in range(end, sta+1):
        result.append(i)
    return result[::-1]
        
    