def solution(m, n, startX, startY, balls):
    answer = []
    
    for a, b in balls:
        candidates = []
        
        # 왼쪽 벽 반사
        if not (startY == b and startX > a):
            candidates.append((startX - (-a))**2 + (startY - b)**2)
        
        # 오른쪽 벽 반사
        if not (startY == b and startX < a):
            candidates.append((startX - (2*m - a))**2 + (startY - b)**2)
        
        # 아래쪽 벽 반사
        if not (startX == a and startY > b):
            candidates.append((startX - a)**2 + (startY - (-b))**2)
        
        # 위쪽 벽 반사
        if not (startX == a and startY < b):
            candidates.append((startX - a)**2 + (startY - (2*n - b))**2)
        
        answer.append(min(candidates))
    
    return answer
