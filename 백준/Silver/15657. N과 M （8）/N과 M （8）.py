n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
visited = [False] * n
n_arr.sort()
answer = []

def dfs(depth, start, arr):

    if depth == m:
        answer.append(arr)
        return

    for i in range(start, n):
        dfs(depth + 1, i, arr + [n_arr[i]])

dfs(0, 0, [])

for n in answer:
    print(*n)