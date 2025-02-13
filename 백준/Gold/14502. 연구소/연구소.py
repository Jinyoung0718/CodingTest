from itertools import combinations
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
empty_space = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
virus_space = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]
answer = 0

def bfs(graph):
    queue = deque(virus_space)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
                    graph[next_x][next_y] = 2
                    queue.append((next_x, next_y))

    return sum(row.count(0) for row in graph)

for walls in combinations(empty_space, 3):
    new_graph = [row[:] for row in graph]
    for x, y in walls:
        new_graph[x][y] = 1

    temp = bfs(new_graph)
    answer = max(answer, temp)

print(answer)