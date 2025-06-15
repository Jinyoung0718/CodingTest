n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()
answer = []

def dfs(depth, arr):

    if depth == m:
        answer.append(arr)
        return

    for i in range(n):
        dfs(depth + 1, arr + [n_arr[i]])

dfs(0, [])

for n in answer:
    print(*n)