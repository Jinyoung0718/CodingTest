def solution(num):
    result1 = ""
    result2 = ""
    for i in num:
        if i % 2 != 0:
            result1 += str(i)
        else:
            result2 += str(i)
        
    return int(result1) + int(result2)