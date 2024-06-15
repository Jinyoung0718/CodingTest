def solution(arr, queries):
    result = []
    
    for query in queries:
        s, e, k = query
        temp = []
        
        for i in range(s, e+1):
            if arr[i] > k:
                temp.append(arr[i])
                
        if temp:
            result.append(min(temp))
        else:
            result.append(-1)
                      
    return result
                      
                      