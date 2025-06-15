from collections import deque

n, m = map(int, input().split())
graph = [[0] * (m + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    row = list(map(int, input()))
    for j in range(1, m + 1):
        graph[i][j] = row[j - 1]

# visited[x][y][chance] → chance=0이면 이미 벽을 한 번 부순 상태
visited = [[[False] * 2 for _ in range(m + 2)] for _ in range(n + 2)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0, 1))  # (x좌표, y좌표, 이동 거리, chance: 1=벽 부술 기회 있음)
    visited[x][y][1] = True

    while queue:
        cur_x, cur_y, dist, chance = queue.popleft()

        if cur_x == n and cur_y == m:
            return dist + 1

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m:
                if graph[nx][ny] == 0 and not visited[nx][ny][chance]:
                    visited[nx][ny][chance] = True
                    queue.append((nx, ny, dist + 1, chance))

                elif graph[nx][ny] == 1 and chance == 1 and not visited[nx][ny][0]:
                    visited[nx][ny][0] = True
                    queue.append((nx, ny, dist + 1, 0))

    return -1

print(bfs(1, 1))