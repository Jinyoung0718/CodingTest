def solution(part, comp):
    
    part.sort()
    comp.sort()
    
    for par, com in zip(part, comp):
        
        if par != com:
            return par
        
    return part[-1]