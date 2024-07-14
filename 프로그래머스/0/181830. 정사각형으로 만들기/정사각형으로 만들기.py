def solution(arr):
    
    for item in arr:
        if len(arr) > len(item):
            for item in arr:
                for _ in range(len(arr) - len(item)):
                    item += [0]
            return arr
        
        elif len(arr) < len(item):
            for _ in range(len(item) - len(arr)):
                arr.append([0] * len(item))
            return arr
                
        elif len(arr) == len(item):
            return arr