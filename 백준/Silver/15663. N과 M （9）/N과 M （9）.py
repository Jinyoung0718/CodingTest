def dfs(depth, temp):
    global  result

    if depth == m:
        result.append(temp)
        return

    prev = 0
    for i in range(n):
        if not visited[i] and arr[i] != prev:
            prev = arr[i]
            visited[i] = True
            dfs(depth + 1, temp + [arr[i]])
            visited[i] = False

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (n + 1)
result = []
dfs(0, [])

for i in result:
    print(*i)