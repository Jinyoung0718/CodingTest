from collections import deque

M, N, K = map(int, input().split())  # M: 세로, N: 가로
graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
answer = []

dx = [-1, 0, 1, 0]  # 상, 좌, 하, 우
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            area = bfs(i, j)
            answer.append(area)

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))