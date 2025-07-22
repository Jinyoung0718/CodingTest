from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_rain = max(map(max, graph))
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, visited, rain):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y] and graph[next_x][next_y] > rain:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

for rain in range(0, max_rain + 1):
    safe_area = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                bfs(i, j, visited, rain)
                safe_area += 1

    answer = max(answer, safe_area)

print(answer)