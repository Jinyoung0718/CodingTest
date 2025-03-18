from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0

def bfs(x, y, rain):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if graph[next_x][next_y] > rain and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

for rain in range(0, max(map(max, graph)) + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                bfs(i, j, rain)
                count += 1

    answer = max(answer, count)

print(answer)