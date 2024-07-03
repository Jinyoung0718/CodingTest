def solution(strArr):
    result = []
    
    for i in range (len(strArr)):
        if "ad" not in strArr[i]:
            result.append(strArr[i])
    return result