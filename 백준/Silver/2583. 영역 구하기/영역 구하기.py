from collections import deque

m, n, k = map(int, input().split()) 
graph = [[0] * n for _ in range(m)] 

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())  
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[m - i - 1][j] = -1  

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 1 
    area = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1 
                    queue.append((nx, ny))
                    area += 1

    return area

areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:  
            areas.append(bfs(i, j))

areas.sort()
print(len(areas))
print(*areas)
