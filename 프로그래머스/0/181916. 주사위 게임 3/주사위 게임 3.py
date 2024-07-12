def solution(a, b, c, d):
    lis = [a, b, c, d]
    cnt = [lis.count(item) for item in lis]
    print(cnt)
    
    if max(cnt) == 4:
        return 1111*a
    elif max(cnt) == 3:
        return (10 * lis[cnt.index(3)] + lis[cnt.index(1)])**2
    elif max(cnt) == 2:
        if 1 in cnt:
            return lis[cnt.index(1)] * lis[cnt.index(1, cnt.index(1)+1, 4)]
        else:
            for i in lis:
                if i != a:
                    return (a+i) * abs(a-i)
    else:
        return min(lis)                
            