from collections import deque

n, m = map(int, input().split())
graph = [[0] * (m + 2)] + [[0] + list(map(int, input())) + [0] for _ in range(n)] + [[0] * (m + 2)]
visited = [[[False] * 2 for _ in range(m + 2)] for _ in range(n + 2)]
# 0-index: 벽 부순 경로, 1-index: 벽을 안 부순 경로

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1, 1)) # x, y, 거리, chance
    visited[x][y][1] = True
    while queue:
        cur_x, cur_y, dist, chance = queue.popleft()

        if cur_x == n and cur_y == m:
            return dist

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m:
                if graph[nx][ny] == 0 and not visited[nx][ny][chance]:
                    visited[nx][ny][chance] = True
                    queue.append((nx, ny, dist + 1, chance))

                elif graph[nx][ny] == 1 and not visited[nx][ny][0] and chance > 0:
                    visited[nx][ny][0] = True
                    queue.append((nx, ny, dist + 1, chance - 1))

    return -1

print(bfs(1, 1))