def solution(my_string):
    
    result = [0]*52
    
    for s in my_string:
        if 65 <= ord(s) <= 90:
            result[ord(s)-65] += 1
        elif 97 <= ord(s) <= 122:
            result[ord(s)-71] += 1
    return result
    