def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(3, total + 1):
        col = i
        row = total // i
        
        if total % i == 0:
            temp_brown = (col + col + row + row) - 4
            temp_yellow = total - temp_brown
            
            if brown == temp_brown and yellow == temp_yellow:
                answer.append(row)
                answer.append(col)
                break
    
    return answer