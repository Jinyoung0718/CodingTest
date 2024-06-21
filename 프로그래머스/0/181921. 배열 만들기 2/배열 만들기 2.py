def solution(l, r):
    result = []
    for num in range(l, r+1):
        if not set(str(num)) - set(['0', '5']):
            result.append(num)
            
    return result if result else [-1]