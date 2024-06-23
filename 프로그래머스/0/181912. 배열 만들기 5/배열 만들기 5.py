def solution(intStrs, k, s, l):
    result = []
    
    for strNum in intStrs:
        temp = strNum[s:s+l]
        if int(temp) > k:
            result.append(int(temp))
    
    return result
