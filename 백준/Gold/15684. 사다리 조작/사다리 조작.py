def check():
    for i in range(1, n + 1):
        temp = i
        for j in range(1, h + 1):
            if graph[j][temp] == 1:       
                temp += 1
            elif graph[j][temp - 1] == 1:
                temp -= 1
        if temp != i:
            return 0  

    return 1  

def dfs(depth, start_loc):
    global result

    if result == 1:
        return

    if depth == limit:
        if check() == 1:
            result = 1
        return
    
    for i in range(start_loc, count):
        x, y = ladder_loc[i]
        if graph[x][y - 1] == 0 and graph[x][y + 1] == 0:
            graph[x][y] = 1
            dfs(depth + 1, i + 1)
            graph[x][y] = 0  

n, m, h = map(int, input().split())
graph = [[0] * (n + 2) for _ in range(h + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1

ladder_loc = [(i, j) for i in range(1, h+1) for j in range(1, n+1) if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i][j + 1] == 0]
count = len(ladder_loc)

result = -1
for limit in range(4):
    dfs(0, 0)
    if result == 1:
        result = limit
        break

print(result)
