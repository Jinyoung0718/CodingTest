def solution(rank, attend):
    
    lis = []
    
    for i in range(len(attend)):
        if attend[i]:
            lis.append((rank[i], i))
    
    lis.sort()
    print(lis)
    return 10000 * lis[0][1] + 100 * lis[1][1] + lis[2][1]