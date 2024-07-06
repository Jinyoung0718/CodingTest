def solution(arr):
    
    result = 0
    
    while 1:
        temp = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                temp.append(num / 2)
            elif num < 50 and num % 2 != 0 :
                temp.append((num * 2) + 1)
            else:
                temp.append(num)
        if arr == temp:
            break
        else:
            arr = temp
            result += 1
            
    return result
            