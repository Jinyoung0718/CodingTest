def solution(strArr):
    
    result = 0
    dic = {}
    
    for s in strArr:
        if len(s) in dic.keys():
            dic[len(s)] += 1
        else:
            dic[len(s)] = 1
    result = max(dic.values())
    
    return result