from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
row = len(graph)
col = len(graph[0])
visited = [[False] * col for _ in range(row)]


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True
    bfs_result = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x =  cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < row and 0 <= next_y < col:
                if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    bfs_result += 1

    return bfs_result

appartment_arr = []

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1 and not visited[i][j]:
            appartment_arr.append(bfs(i, j))

print(len(appartment_arr))

appartment_arr.sort()

for i in appartment_arr:
    print(i)