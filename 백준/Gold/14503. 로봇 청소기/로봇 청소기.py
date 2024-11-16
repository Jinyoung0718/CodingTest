dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, direct = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph[x][y] = -1
result = 1

while True:
    clean = False
    for i in range(4):
        direct = (direct + 3) % 4
        next_x = x + dx[direct]
        next_y = y + dy[direct]
        if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
            graph[next_x][next_y] = -1
            clean = True
            result += 1
            x, y = next_x, next_y
            break

    if not clean:
        if graph[x - dx[direct]][y - dy[direct]] != 1:
            x -= dx[direct]
            y -= dy[direct]
        else:
            print(result)
            break