def solution(arr):
    
    for i in range(11):
        if len(arr) < 2**i:
            dist = 2**i - len(arr)
            for _ in range(dist):
                arr.append(0)
            break
        elif len(arr) == 2**i:
            break
            
    return arr