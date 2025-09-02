from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 빙산 덩어리 세기용 BFS
def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited.add((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited and graph[nx][ny] > 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

# 빙산 녹이기 (temp 제거 버전)
def melt():
    sea_list = []  # (좌표, 주변 바다 수)
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        sea += 1
                sea_list.append((i, j, sea))
    
    # 계산된 sea 값을 한꺼번에 반영
    for x, y, sea in sea_list:
        graph[x][y] = max(graph[x][y] - sea, 0)

while True:
    visited = set()
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and (i, j) not in visited:
                bfs(i, j, visited)
                count += 1

    if count == 0:  # 빙산이 다 녹은 경우
        print(0)
        break

    if count >= 2:  # 덩어리가 2개 이상으로 쪼개진 경우
        print(year)
        break

    melt()  # 한 해 동안 녹이기
    year += 1
