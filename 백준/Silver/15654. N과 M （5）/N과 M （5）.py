def dfs(depth, temp):
    global  result

    if depth == m:
        result.append(temp)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, temp + [arr[i]])
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * (n + 1)
result = []
dfs(0, [])

result.sort()

for i in result:
    print(*i)