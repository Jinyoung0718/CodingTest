n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

visited[r][c] = 1
count = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d + 3) % 4
        next_r = r + dx[d]
        next_c = c + dy[d]
        if 0 <= next_r < n and 0 <= next_c < m and graph[next_r][next_c] == 0:
            if visited[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                count += 1
                r = next_r
                c = next_c
                flag = 1
                break
    
    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r - dx[d], c - dy[d]