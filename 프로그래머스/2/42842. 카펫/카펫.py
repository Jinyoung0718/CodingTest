def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for num in range(3, total):
        
        col = num
        row = total // num
        
        if total % num == 0:
            b = col + col + row + row - 4
            y = total - b
            
            if b == brown and y == yellow:
                answer.append(row)
                answer.append(col)
                break
    
    return answer
        
        