from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty_spaces = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
virus_positions = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

def bfs(graph_copy):
    queue = deque(virus_positions)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                queue.append((nx, ny))
    return sum(row.count(0) for row in graph_copy)

max_safe_area = 0

for walls in combinations(empty_spaces, 3):

    graph_copy = copy.deepcopy(graph)
    for x, y in walls:
        graph_copy[x][y] = 1
    safe_area = bfs(graph_copy)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
