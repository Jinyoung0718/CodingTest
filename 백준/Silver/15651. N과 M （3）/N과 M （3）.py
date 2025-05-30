n, m = map(int, input().split())
answer = []

def dfs(depth, arr):

    if depth == m:
        answer.append(arr)
        return

    for i in range(1, n + 1):
        dfs(depth + 1, arr + [i])

dfs(0, [])

for lst in answer:
    print(*lst)