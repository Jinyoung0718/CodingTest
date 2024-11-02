from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
result = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 0)]) 
    visited = set()
    visited.add((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count > 10: 
            return -1

        if graph[rx][ry] == 'O' and graph[bx][by] != 'O':  
            return count

        for i in range(4):  

            # 빨강이
            next_rx, next_ry = rx, ry
            while graph[next_rx + dx[i]][next_ry + dy[i]] != '#' and graph[next_rx][next_ry] != 'O':
                next_rx += dx[i]
                next_ry += dy[i]

            # 파랑이
            next_bx, next_by = bx, by
            while graph[next_bx + dx[i]][next_by + dy[i]] != '#' and graph[next_bx][next_by] != 'O':
                next_bx += dx[i]
                next_by += dy[i]

            if graph[next_bx][next_by] == 'O':  
                continue

            if next_rx == next_bx and next_ry == next_by:
                if abs(next_rx - rx) + abs(next_ry - ry) > abs(next_bx - bx) + abs(next_by - by):
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.add((next_rx, next_ry, next_bx, next_by))
                queue.append((next_rx, next_ry, next_bx, next_by, count + 1))

    return -1  

print(bfs(rx, ry, bx, by))