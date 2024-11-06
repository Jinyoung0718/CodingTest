from collections import deque

n = int(input())
graph = [input() for _ in range(n)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_normal(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if graph[next_x][next_y] == graph[cur_x][cur_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def bfs_colorblind(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if (graph[next_x][next_y] == graph[cur_x][cur_y]) or (graph[next_x][next_y] in 'RG' and graph[cur_x][cur_y] in 'RG'):
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))


temp = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_normal(i, j)
            temp += 1

result.append(temp)

temp = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_colorblind(i, j)
            temp += 1

result.append(temp)

print(*result)