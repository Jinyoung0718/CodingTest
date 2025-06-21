from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0
            break

size = 2
eat_count = 0
total_time = 0

def bfs(x, y, size):
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    fish_list = []

    while queue:
        x, y, dist = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 지나갈 수 있는 조건: 상어 크기 이상은 못 지나감
                if graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

                    # 먹을 수 있는 물고기라면 후보로 저장
                    if 0 < graph[nx][ny] < size:
                        fish_list.append((dist + 1, nx, ny))

    if not fish_list:
        return None

    fish_list.sort()  # 거리, x(위), y(왼쪽) 우선순위로 정렬
    return fish_list[0]

while True:
    result = bfs(shark_x, shark_y, size)

    if result is None:
        break

    dist, fx, fy = result
    total_time += dist
    eat_count += 1
    graph[fx][fy] = 0
    shark_x, shark_y = fx, fy  # 상어 위치 이동

    if eat_count == size:
        size += 1
        eat_count = 0

print(total_time)