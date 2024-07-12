def solution(mys, ind):
    
    lis = list(mys)
    ind.sort(reverse=True)
    for i in ind:
        lis.pop(i)
        
    return ''.join(lis)
        