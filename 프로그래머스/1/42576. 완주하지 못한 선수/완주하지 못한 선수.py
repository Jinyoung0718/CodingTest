def solution(part, comple):
    
    part.sort()
    comple.sort()
    for i in range(0, len(comple)):
        if part[i] != comple[i]:
            return part[i]
    return part[-1]