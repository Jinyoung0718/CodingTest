def solution(rank, attend):
    result = []
    for i in range(len(attend)):
        
        if attend[i] == 1:
            result.append((rank[i], i ))
            
    result.sort()
    return 10000 * result[0][1] + 100 * result[1][1] + result[2][1]
    