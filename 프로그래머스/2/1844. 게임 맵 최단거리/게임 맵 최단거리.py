from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))
        visited[x][y] = True

        while queue:
            cur_x, cur_y, dist = queue.popleft()
            if cur_x == n - 1 and cur_y == m - 1:
                return dist

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
        
        return -1

    return bfs(0, 0)