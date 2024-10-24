def dfs(depth):
    global result

    if depth == M:
        result = max(result, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            check = int(''.join(arr))

            if (depth, check) not in visited:
                visited.append((depth, check))
                dfs(depth + 1)

            arr[i], arr[j] = arr[j], arr[i]

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    result = 0
    dfs(0)

    print(f"#{case} {result}")
