def dfs(depth, start, temp):
    global  result

    if depth == m:
        result.append(temp)
        return

    for i in range(start, n + 1):
        dfs(depth + 1, i + 1, temp + [i])


n, m = map(int, input().split())
result = []
dfs(0, 1, [])

for i in result:
    print(*i)