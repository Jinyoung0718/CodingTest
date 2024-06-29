def solution(my_string):
    
    result = [0] * 52
    
    for num in my_string:
        if num.isupper():
            k = 65
            result[ord(num) - k] +=1
        else:
            k = 71
            result[ord(num) - k] +=1
    return result