def solution(a, d, included):
    result = 0
    
    for i in range(0, len(included)):
        if included[i] == True:
            result += a + (d*i)
    return result