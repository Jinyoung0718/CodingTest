n, m = map(int, input().split())
target = int(input())
graph = [[0] * n for _ in range(m)]
result = []

num = 1
x, y = 0, 0
direction = 0
find = False

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while num <= n * m:
    graph[x][y] = num

    if num == target:
        find = True
        print(*(y + 1, x + 1))
        break

    next_x = x + dx[direction]
    next_y = y + dy[direction]

    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or graph[next_x][next_y] != 0:
        direction = (direction + 1) % 4
        next_x = x + dx[direction]
        next_y = y + dy[direction]
    
    x, y = next_x, next_y
    num += 1

if not find: print(0)