from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[m - i - 1][j] = -1
            visited[m - i - 1][j] = True
    # 리스트 는 위에서 아래로(0 → m-1) 증가 하는 반면, 좌표계 는 아래_에서 위로(m-1 → 0) 증가

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cur_len = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if graph[next_x][next_y] != -1 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
                    cur_len += 1

    return cur_len

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(" ".join(map(str, answer)))