def solution(part, comp):
    
    dic = {}
    sum_hash = 0
    
    for par in part:
        val = hash(par)
        dic[val] = par
        sum_hash += val
    
    for com in comp:
        val = hash(com)
        sum_hash -= val
    return dic[sum_hash]