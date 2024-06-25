def solution(my_string, queries):
    
    lis = list(my_string)
    
    for s, e in queries:
        lis[s:e+1] = lis[s:e+1][::-1]
    return ''.join(lis)
        