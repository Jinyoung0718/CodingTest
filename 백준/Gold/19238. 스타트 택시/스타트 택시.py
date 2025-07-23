from collections import deque

n, m, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tx, ty = map(int, input().split())
tx -= 1
ty -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

destinations = [(0, 0)] * (m + 1)

for i in range(1, m + 1):
    sx, sy, ex, ey = map(int, input().split())
    graph[sx - 1][sy - 1] = -i
    destinations[i] = (ex - 1, ey - 1)

# 가장 가까운 승객 찾기
def bfs_passenger(sx, sy):
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((sx, sy, 0))
    visited[sx][sy] = True
    candidates = []

    while queue:
        x, y, dist = queue.popleft()
        if graph[x][y] < 0:  # 승객 발견
            candidates.append((dist, x, y, -graph[x][y]))  # 거리, 행, 열, 승객번호(-를 붙여 부호 반전)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    if not candidates:
        return None

    candidates.sort()

    # 승객이 여러 명이면 그중 행 번호가 가장 작은 승객 -> x
    # 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객 -> y
    return candidates[0]  # (거리, x, y, 승객 번호)

# 목적지까지 이동
def bfs_destination(sx, sy, ex, ey):
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((sx, sy, 0))
    visited[sx][sy] = True

    while queue:
        x, y, dist = queue.popleft()
        
        if x == ex and y == ey:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                
    return -1

# 메인 로직
for _ in range(m):
    result = bfs_passenger(tx, ty)

    if result is None:
        print(-1)
        exit()

    dist_to_passenger, px, py, pid = result

    if fuel < dist_to_passenger:
        print(-1)
        exit()

    fuel -= dist_to_passenger
    graph[px][py] = 0  # 승객 태움
    dest_x, dest_y = destinations[pid]

    dist_to_dest = bfs_destination(px, py, dest_x, dest_y)
    
    if dist_to_dest == -1 or fuel < dist_to_dest:
        print(-1)
        exit()

    fuel -= dist_to_dest
    fuel += dist_to_dest * 2
    tx, ty = dest_x, dest_y  # 택시 위치 갱신

print(fuel)