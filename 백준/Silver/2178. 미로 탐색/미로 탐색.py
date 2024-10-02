from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]

queue = deque()
queue.append((0, 0, 1))
visited[0][0] = True

while queue:
    cur_x, cur_y, cur_distance =queue.popleft()

    if cur_x == N - 1 and cur_y == M - 1:
        print(cur_distance)
        break

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M: 
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, cur_distance + 1))