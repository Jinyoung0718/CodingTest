n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def dfs(index, total, count):
    global answer

    if index == n:
        if total == s and count > 0:
            answer += 1
        return

    dfs(index + 1, total + arr[index], count + 1)
    dfs(index + 1, total, count)

dfs(0, 0, 0)
print(answer)