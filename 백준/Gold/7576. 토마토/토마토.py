from collections import deque

n, m = map(int, input().split())
queue = deque()
tomato = []


for _ in range(m):
    tomato_row = list(map(int, input().split()))
    tomato.append(tomato_row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if tomato[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                    tomato[next_x][next_y] = tomato[cur_x][cur_y] + 1

bfs()
max_days = 0

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        max_days = max(max_days, tomato[i][j])

print(max_days - 1)