def solution(arr, comm):
    result = []
    
    for i, j, k in comm:  
        sort_arr = sorted(arr[i-1:j])  
        result.append(sort_arr[k-1])  
    
    return result
