from collections import deque

row, col, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(col)] for _ in range(h)]
visited = [[[False] * row for _ in range(col)] for _ in range(h)]
queue = deque()
answer = 0
temp = 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for layer in graph:
    for line in layer:
        temp += line.count(0)

if temp == 0:
    print(0)
    exit()

for i in range(h):
    for j in range(col):
        for k in range(row):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    cur_z, cur_x, cur_y = queue.popleft()
    for i in range(6):
        next_z = cur_z + dz[i]
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if 0 <= next_x < col and 0 <= next_y < row and 0 <= next_z < h:
            if not visited[next_z][next_x][next_y] and graph[next_z][next_x][next_y] == 0:
                visited[next_z][next_x][next_y] = True
                graph[next_z][next_x][next_y] = graph[cur_z][cur_x][cur_y] + 1
                queue.append((next_z, next_x, next_y))

for i in range(h):
    for j in range(col):
        for k in range(row):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            answer = max(answer, graph[i][j][k])

print(answer - 1)