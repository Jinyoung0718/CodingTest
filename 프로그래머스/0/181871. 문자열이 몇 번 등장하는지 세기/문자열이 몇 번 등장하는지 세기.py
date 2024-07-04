def solution(myString, pat):
    
    result = 0
    leng = len(pat)
    for i in range(len(myString)):
        if myString[i:i+leng] == pat:
            result += 1
    return result