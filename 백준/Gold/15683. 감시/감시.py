dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_direction = [[], [1], [3, 1], [0, 1], [0, 1, 3], [0, 1, 2, 3]]

n, m = map(int, input().split())
graph = [[6] * (m+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(n)] + [[6] * (m + 2)]
cctv_loc = [(i, j) for i in range(n + 2) for j in range(m + 2) if 1 <= graph[i][j] <= 5]
limit = len(cctv_loc)
result = n * m

def check(temp):
    visited = [[False] * (m + 2) for _ in range(n + 2)]

    for i in range(limit):
        cctv_x, cctv_y = cctv_loc[i]
        rotate = temp[i]
        cctv = graph[cctv_x][cctv_y]

        for direct in cctv_direction[cctv]:
            direct = (direct + rotate) % 4
            next_x, next_y = cctv_x, cctv_y
            while True:
                next_x, next_y = next_x + dx[direct], next_y + dy[direct]
                if graph[next_x][next_y] == 6:
                    break
                visited[next_x][next_y] = True
        
    count = 0
    for i in range(n+2):
        for j in range(m+2):
            if graph[i][j] == 0 and visited[i][j] == False:
                count += 1
    
    return count

def dfs(depth, temp):
    global result

    if depth == limit:
        result = min(result, check(temp))
        return
    
    dfs(depth + 1, temp + [0])
    dfs(depth + 1, temp + [1])
    dfs(depth + 1, temp + [2])
    dfs(depth + 1, temp + [3])

dfs(0, [])
print(result)