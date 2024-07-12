def solution(n, k):
    temp = n//k
    result = []
    
    for i in range(1, temp+1):
        result.append(k*i)
    return result