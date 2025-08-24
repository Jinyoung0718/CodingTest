from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    col_sum = [0] * m
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                size = 0
                cols = set()
                
                while queue:
                    cur_x, cur_y = queue.popleft()
                    size += 1
                    cols.add(cur_y)
                    
                    for d in range(4):
                        nx = cur_x + dx[d]
                        ny = cur_y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
            
                for c in cols:
                    col_sum[c] += size
    
    return max(col_sum)