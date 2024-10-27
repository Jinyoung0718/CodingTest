from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def change_bfs(x, y):
    temp = 0
    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N and arr[next_x][next_y] == '*':
            temp += 1
    arr[x][y] = temp

def count_check(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True  

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(8):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                if arr[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                visited[next_x][next_y] = True


for testcase in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                change_bfs(i, j)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and not visited[i][j]:
                result += 1
                count_check(i, j)

    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*' and not visited[i][j]:
                result += 1

    print(f'#{testcase} {result}')
