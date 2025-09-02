from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = set()
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited.add((x, y))
        total = int(maps[x][y])
        
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        total += int(maps[nx][ny])
                        queue.append((nx, ny))
                        
        return total
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and (i, j) not in visited:
                result = bfs(i, j)
                answer.append(result)
    
    if not answer:
        return [-1]
    
    return sorted(answer)