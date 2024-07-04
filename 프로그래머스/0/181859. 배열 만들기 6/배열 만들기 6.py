def solution(arr):
    result = []
    i = 0
    
    while i < len(arr):
        
        if len(result) == 0:
            result += [arr[i]]
            i += 1
        elif len(result) != 0 and result[-1] == arr[i]:
            result.pop()
            i += 1
        elif len(result) != 0 and result[-1] != arr[i]:
            result.append(arr[i])
            i += 1
    return result if result else [-1]