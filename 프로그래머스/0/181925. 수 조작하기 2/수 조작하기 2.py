def solution(num):
    result = ""
    dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    for i in range(1, len(num)):
        result += dict[num[i] - num[i-1]]
    
    return result
    