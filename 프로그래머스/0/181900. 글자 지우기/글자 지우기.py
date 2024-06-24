def solution(my_string, indices):
    
    lis = list(my_string)
    indices.sort(reverse=True)
    
    for i in range(0, len(indices)):
        a = indices[i]
        print(a)
        lis.pop(a)
    return ''.join(lis)