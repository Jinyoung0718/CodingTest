def solution(myString):
    lis = sorted(myString.split("x"))
    
    return  [cha for cha in lis if cha]