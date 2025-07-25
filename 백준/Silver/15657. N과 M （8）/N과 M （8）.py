n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []

def dfs(depth, start, arr):

    if depth == m:
        answer.append(arr)
        return

    for i in range(start, n):
        dfs(depth + 1, i, arr + [lst[i]])

dfs(0, 0,[])

for row in answer:
    print(*row)