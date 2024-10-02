from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
duration = 0

visited = [[False] * m for _ in range(n)]

def bfs(x, y, leng):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = True
    queue = deque()
    queue.append((x, y, leng))
    while queue:
        cur_x, cur_y, cur_len = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            print(cur_len)
            break
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_len+1)) 

bfs(0, 0, 1)