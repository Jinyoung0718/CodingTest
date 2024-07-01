def solution(myString, pat):
    
    myString = myString.upper()
    pat = pat.upper()
    
    if len(myString) < len(pat):
        return 0
    
    return 1 if pat in myString else 0