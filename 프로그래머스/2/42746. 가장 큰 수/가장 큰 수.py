from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key = cmp_to_key(compare))
    
    if numbers_str[0] == '0':
        return '0'
    
    return ''.join(numbers_str)