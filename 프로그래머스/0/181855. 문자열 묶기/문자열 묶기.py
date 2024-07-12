def solution(strArr):
    dic = {}
    
    for i in strArr:
        
        if len(i) in dic.keys():
            dic[len(i)] += 1
        else:
            dic[len(i)] = 1
    return max(dic.values())