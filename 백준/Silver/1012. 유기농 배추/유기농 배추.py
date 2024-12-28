import sys

sys.setrecursionlimit(10 ** 6)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < col and 0 <= ny < row:
            if a[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

t = int(input())
for _ in range(t):
    answer = 0
    row, col, k = map(int, input().split())
    a = [[0] * row for _ in range(col)]
    visited = [[False] * row for _ in range(col)]

    for _ in range(k):
        x, y = map(int, input().split())
        a[y][x] = 1

    for i in range(col):
        for j in range(row):
            if a[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)