def solution(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                print(arr[i][j], arr[j][j])
                return 0
    return 1
            