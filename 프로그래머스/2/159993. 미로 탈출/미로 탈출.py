from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    answer = 0
    
    dist1, dist2 = 0, 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            
            if maps[i][j] == 'L':
                rx, ry = i, j
            
            if maps[i][j] == 'E':
                ex, ey = i, j
    
    def find_leber_bfs(x, y):
        visited = set()
        visited.add((x, y))
        queue = deque()
        queue.append((x, y, 0))
        while queue:
            cur_x, cur_y, cur_len = queue.popleft()
            
            if cur_x == rx and cur_y == ry:
                return cur_len
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and (nx, ny) not in visited:
                        queue.append((nx, ny, cur_len + 1))
                        visited.add((nx, ny))
        
        return -1
            
    
    dist1 += find_leber_bfs(sx, sy)
    
    if dist1 == -1:
        return -1
    
    def find_exit_bfs(x, y):
        visited = set()
        visited.add((x, y))
        queue = deque()
        queue.append((x, y, 0))
        while queue:
            cur_x, cur_y, cur_len = queue.popleft()
            
            if cur_x == ex and cur_y == ey:
                return cur_len
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and (nx, ny) not in visited:
                        queue.append((nx, ny, cur_len + 1))
                        visited.add((nx, ny))
        
        return -1
    
    dist2 += find_exit_bfs(rx, ry)
    
    if dist2 == -1:
        return -1
    
    answer += (dist1 + dist2)
    return answer