from collections import deque

T = int(input())

for _ in range(T):
    row, col, vagi = map(int, input().split())

    graph = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]

    for _ in range(vagi):
        x, y = map(int, input().split())
        graph[x][y] = 1

    def bfs(x, y):

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if 0 <= next_x < row and 0 <= next_y < col:
                    if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    result = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result += 1

    print(result)