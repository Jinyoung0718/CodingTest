n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

def dfs(depth, cur_sum, count):
    global result

    if depth == n:
        if cur_sum == m and count > 0:
            result += 1
        return

    dfs(depth + 1, cur_sum + data[depth], count + 1) 
    dfs(depth + 1, cur_sum, count)       

dfs(0, 0, 0)

print(result)
