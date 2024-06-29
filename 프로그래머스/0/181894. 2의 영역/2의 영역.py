def solution(arr):
    
    if 2 in arr:
        start = arr.index(2)
        end = len(arr) - arr[::-1].index(2)
        return arr[start:end]
    else:
        return [-1]