from collections import deque

col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(col)]
count = 0
last_cheeze = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    visited = [[False] * row for _ in range(col)]
    queue = deque()
    queue.append((0, 0))
    melt = 0
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < col and 0 <= next_y < row:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True

                    if graph[next_x][next_y] == 1:
                        graph[next_x][next_y] = 0
                        melt += 1
                    else:
                        queue.append((next_x, next_y))

    return melt

while True:

    melted = bfs()

    if melted == 0:
        break

    last_cheeze = melted
    count += 1

print(count)
print(last_cheeze)