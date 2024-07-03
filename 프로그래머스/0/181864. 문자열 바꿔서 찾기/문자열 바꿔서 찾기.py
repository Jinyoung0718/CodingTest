def solution(myString, pat):
    
    new = ""
    
    for i in myString:
        if i == "A":
            i = "B"
            new += i
        else:
            i = "A"
            new += i
    
    return 1 if pat in new else 0