n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alpha = set()
answer = 0

def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] not in alpha:
                alpha.add(graph[nx][ny])
                dfs(nx, ny, count + 1)
                alpha.remove(graph[nx][ny])  # 백트래킹

alpha.add(graph[0][0])  # 시작 알파벳 포함
dfs(0, 0, 1)
print(answer)
