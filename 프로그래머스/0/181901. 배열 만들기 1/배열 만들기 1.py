def solution(n, k):
    
    result = []
    a = int(n/k)
    for i in range(1, a+1):
        temp = k*i
        print(temp)
        bo = True
        if temp > n:
            bo = False
            break
        if bo:
            result.append(temp)
    return result