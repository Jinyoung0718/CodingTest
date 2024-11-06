n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_sum = 0

def dfs(x, y, current_sum, depth):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, current_sum)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, current_sum + graph[ny][nx], depth + 1)
            visited[ny][nx] = False

def check_t_shape(x, y):
    global max_sum
    t_sum = graph[y][x]
    arm_values = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            arm_values.append(graph[ny][nx])
    if len(arm_values) == 4:
        max_sum = max(max_sum, t_sum + sum(arm_values) - min(arm_values))
    elif len(arm_values) == 3:
        max_sum = max(max_sum, t_sum + sum(arm_values))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, graph[i][j], 1)
        visited[i][j] = False
        check_t_shape(j, i)

print(max_sum)