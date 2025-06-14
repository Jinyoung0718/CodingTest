def dfs(depth, temp, start):
    if depth == m:
        result.append(temp)
        return

    for i in range(start, n):
        dfs(depth + 1, temp + [arr[i]], i + 1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

dfs(0, [], 0)
result.sort()

for i in result:
    print(*i)
