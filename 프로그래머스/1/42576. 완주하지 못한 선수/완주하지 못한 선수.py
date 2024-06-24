def solution(participant, completion):
    
    hashdict = {}
    sumHash = 0
    
    for part in participant:
        hashdict[hash(part)] = part
        sumHash += hash(part)
        
    for comple in completion:
        sumHash -= hash(comple)
    
    return hashdict[sumHash]
    