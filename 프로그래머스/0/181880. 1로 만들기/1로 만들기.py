def solution(lis):
    result = 0
    
    for num in lis:
        while 1 < num:
            result += 1
            if num % 2 == 0:
                num = num // 2
                if num == 1:
                    break
            else:
                num = (num - 1) // 2
                if num == 1:
                    break
            
    return result
            