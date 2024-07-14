def solution(n):
    if n == 1:
        return [[1]]
    
    result = [[0] * n for _ in range(n)]
    
    x, y = 0, 0
    dir = 'r'
    
    for i in range(n * n):
        result[x][y] = i + 1
        
        if dir == 'r':
            if y + 1 < n and result[x][y + 1] == 0:
                y += 1
            else:
                dir = 'd'
                x += 1
        elif dir == 'd':
            if x + 1 < n and result[x + 1][y] == 0:
                x += 1
            else:
                dir = 'l'
                y -= 1
        elif dir == 'l':
            if y - 1 >= 0 and result[x][y - 1] == 0:
                y -= 1
            else:
                dir = 'u'
                x -= 1
        elif dir == 'u':
            if x - 1 >= 0 and result[x - 1][y] == 0:
                x -= 1
            else:
                dir = 'r'
                y += 1

    return result