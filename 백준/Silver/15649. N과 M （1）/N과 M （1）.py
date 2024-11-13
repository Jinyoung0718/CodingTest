def dfs(depth, temp):
    global  result

    if depth == m:
        result.append(temp)
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, temp + [i])
            visited[i] = False
n, m = map(int, input().split())
visited = [False] * (n + 1)
result = []

dfs(0, [])

for i in result:
    print(*i)