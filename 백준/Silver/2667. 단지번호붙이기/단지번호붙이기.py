from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    count = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if graph[next_x][next_y] != 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    count += 1
    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] != 0:
            result.append(bfs(i, j))

print(len(result))
result.sort()
for num in result:
    print(num)