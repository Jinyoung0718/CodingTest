def solution(myString):
    lis = myString.split("x")
    lis2 = [i for i in lis if i.strip()]
    return sorted(lis2)  