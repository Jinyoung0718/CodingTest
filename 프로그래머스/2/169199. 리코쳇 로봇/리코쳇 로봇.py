from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    sx = sy = gx = gy = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sx, sy = i, j
            elif board[i][j] == 'G':
                gx, gy = i, j

    def bfs(sx, sy):
        visited = set()
        visited.add((sx, sy))
        queue = deque()
        queue.append((sx, sy, 0))
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while queue:
            x, y, count = queue.popleft()
            
            if x == gx and y == gy:
                return count
            
            for i in range(4):
                nx, ny = x, y
                
                # 끝까지 미끄러지기
                while True:
                    tx, ty = nx + dx[i], ny + dy[i]
                    
                    if not (0 <= tx < n and 0 <= ty < m):  # 보드 밖
                        break
                    
                    if board[tx][ty] == 'D':  # 장애물
                        break
                    
                    nx, ny = tx, ty
            
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, count + 1))
        
        return -1
    
    return bfs(sx, sy) 