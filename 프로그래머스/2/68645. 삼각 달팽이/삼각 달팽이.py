def solution(n):
    answer = []
    tri = [[0] * (i + 1) for i in range(n)]
    num = 1
    x, y = -1, 0
    
    for i in range(n):
        for _ in range(i, n):
            
            if i % 3 == 0:      # 아래
                x += 1
            
            elif i % 3 == 1:    # 오른쪽
                y += 1
            
            else:               # 왼쪽 위
                x -= 1
                y -= 1
            
            tri[x][y] = num
            num += 1
            
    for row in tri:
        for num in row:
            answer.append(num)
    
    return answer