from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

empty_space = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
virus_space = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

def bfs(graph):
    queue = deque(virus_space)
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 2
                queue.append((next_x, next_y))

    return sum(row.count(0) for row in graph)

temp = 0
for walls in combinations(empty_space, 3):
    copy_graph = [row[:] for row in graph]
    for x, y in walls:
        copy_graph[x][y] = 1

    temp = bfs(copy_graph)
    result = max(temp, result)

print(result)